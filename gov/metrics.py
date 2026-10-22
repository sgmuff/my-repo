"""Count the program's key metrics from gov records and deliverable metadata.

Usage:
  gov metrics <output-root> --as-of YYYY-MM-DD [--since YYYY-MM-DD] [--out FILE]

Reads every gov record (*.yaml) under the output root (default compliance/),
with the same derived values `gov render` uses, plus the metadata block of
Markdown deliverables gov doesn't manage yet (program assessments, policies,
regulatory change memos). Writes <output-root>/reports/metrics-YYYY-MM-DD.md
(or --out). Every number lists the files it was counted from, so each figure
in a leadership report can be traced to a record. --since sets the start of
the reporting period (default 90 days before --as-of) for "new this period"
counts.

It counts what the records say. It doesn't judge whether a record is right,
and a count of zero can mean the register is incomplete.
"""
import argparse
import datetime as dt
import os
import re
import sys
from collections import Counter, defaultdict

DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")
SKIP = ("index.md", "schedule.md")
# A record is finished only when closed or retired; an approved record still has reviews and accepted risks.
CLOSED = ("closed", "done", "verified", "retired", "cancelled", "responded", "superseded")
RATINGS = ("High", "Medium", "Low")


def meta(text):
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        return None
    out = {}
    for line in m.group(1).splitlines():
        if not line or line[0] in " \t-#":
            continue
        k, sep, v = line.partition(":")
        if sep:
            out[k.strip()] = re.sub(r"\s+#.*$", "", v).strip()
    return out


def date_of(v):
    d = DATE.search(str(v or ""))
    return dt.date.fromisoformat(d.group(1)) if d else None


def is_open(status):
    return not any(c in (status or "").lower() for c in CLOSED)


def load_records(root):
    """(rel, data, derived) for every gov record under root, and (rel, metadata) for unmanaged Markdown deliverables."""
    import yaml
    from gov.derive import DERIVE
    records, docs = [], []
    for dirpath, dirs, names in os.walk(root):
        dirs[:] = [d for d in dirs if d not in (".gov", "reports")]
        for n in sorted(names):
            p = os.path.join(dirpath, n)
            rel = os.path.relpath(p, root)
            if n.endswith(".yaml"):
                try:
                    data = yaml.safe_load(open(p, encoding="utf-8"))
                except (OSError, UnicodeDecodeError, yaml.YAMLError):
                    continue
                if isinstance(data, dict) and data.get("type") in DERIVE:
                    try:
                        derived = DERIVE[data["type"]](data)
                    except (KeyError, TypeError, ValueError):
                        derived = {}  # an invalid record; gov validate reports it
                    records.append((rel, data, derived))
            elif n.endswith(".md") and n not in SKIP and not n.endswith(("-notices.md", "-drafts.md", "-requests.md")):
                if os.path.exists(p[:-3] + ".yaml"):
                    continue  # rendered from a record
                try:
                    md = meta(open(p, encoding="utf-8").read())
                except (OSError, UnicodeDecodeError):
                    continue
                if md is not None:
                    docs.append((rel, md))
    return records, docs


def status_of(data):
    if data.get("lifecycle") == "retired":
        return "Retired"
    if data["type"] == "inc" and date_of((data.get("closure") or {}).get("closed")):
        return "Closed"
    return str(data.get("status", "unknown"))


def started(data):
    if data["type"] == "dsr":
        return date_of(data["received"]["date"])
    if data["type"] == "inc":
        return date_of(data["awareness"]["time"]) or date_of(data.get("date_prepared"))
    return date_of(data.get("date_prepared"))


def main(argv=None):
    from gov import risk
    ap = argparse.ArgumentParser(prog="gov metrics", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("root")
    ap.add_argument("--as-of", required=True, help="YYYY-MM-DD: the end of the reporting period; gov never reads the clock")
    ap.add_argument("--since")
    ap.add_argument("--out")
    a = ap.parse_args(argv)
    if not os.path.isdir(a.root):
        sys.exit(f"Not a folder: {a.root}")
    today = dt.date.fromisoformat(a.as_of)
    since = dt.date.fromisoformat(a.since) if a.since else today - dt.timedelta(days=90)
    records, docs = load_records(a.root)
    of = lambda t: [(rel, d, x) for rel, d, x in records if d["type"] == t]

    by_type = Counter()
    by_type_status = defaultdict(Counter)
    new_this_period = Counter()
    for rel, data, _ in records:
        t = data["type"]
        by_type[t] += 1
        by_type_status[t][status_of(data)] += 1
        s = started(data)
        if s and since <= s <= today:
            new_this_period[t] += 1
    for rel, md in docs:
        t = md.get("type", "unknown")
        by_type[t] += 1
        by_type_status[t][md.get("status", "unknown")] += 1
        s = date_of(md.get("date_prepared"))
        if s and since <= s <= today:
            new_this_period[t] += 1

    # Overdue dates on open records
    overdue = []
    for rel, data, x in records:
        if not is_open(status_of(data)):
            continue
        dates = {"next review": data.get("next_review"), "next test": data.get("next_test")}
        if data["type"] == "dsr":
            dates["deadline"] = x.get("due")
        if data["type"] == "inc" and x.get("earliest"):
            dates["earliest deadline"] = x["earliest"]["due"]
        for k, v in dates.items():
            d = date_of(v)
            if d and d < today:
                overdue.append((d, data["id"], k, rel))
    for rel, md in docs:
        if is_open(md.get("status")):
            for k in ("next_review", "due"):
                d = date_of(md.get(k))
                if d and d < today:
                    overdue.append((d, md.get("id", rel), k.replace("_", " "), rel))
    overdue.sort()

    # Risks and actions
    risks, actions_overdue, blockers_open, assessed = [], [], [], []
    for rel, data, x in records:
        doc_open = is_open(status_of(data))
        for k in data.get("risks") or []:
            rating = risk.rate(k["current"])
            if rating in RATINGS and doc_open:
                risks.append((rating, k["id"], data["id"], rel, k["risk"][:90]))
        for act in data.get("actions") or []:
            if act["status"] != "open":
                continue
            d = date_of(act["due"])
            if d and d < today:
                actions_overdue.append((d, act["id"], data["id"], rel))
            if act["launch_blocking"] and doc_open:
                blockers_open.append((act["id"], data["id"], act.get("block_reason", ""), rel))
        if data.get("risks") and x.get("current") in RATINGS:
            assessed.append((data["type"], data["id"], x["current"], bool(x.get("confirmed")), data["status"], rel))
    risk_counts = Counter(r[0] for r in risks)

    # DSRs
    dsr = of("dsr")
    dsr_on_time, dsr_late, dsr_open_late, dsr_days, sla_met, sla_missed = [], [], [], [], [], []
    for rel, data, x in dsr:
        resp, dl, target = date_of(data["responded"]), date_of(x.get("due")), date_of(data["internal_target"])
        if resp and dl:
            (dsr_on_time if resp <= dl else dsr_late).append(rel)
        if x.get("days_to_respond") is not None:
            dsr_days.append(x["days_to_respond"])
        elif dl and dl < today and is_open(data["status"]):
            dsr_open_late.append(rel)
        if target and (resp or target < today):
            (sla_met if resp and resp <= target else sla_missed).append(rel)

    # Incidents
    inc = of("inc")
    inc_breach = [rel for rel, data, _ in inc if data["breach"]["value"] is True]
    inc_open = [rel for rel, data, _ in inc if is_open(data["status"])]

    # Vendors: a review's slug is its file name after the ID
    vr = of("vr")
    reviewed = {os.path.basename(rel)[12:-5] for rel, _, _ in vr}
    used = set()
    from gov.derive import vendor_slugs
    for rel, data, _ in of("ropa"):
        try:
            used.update(vendor_slugs(data))
        except (KeyError, TypeError):
            pass
    unreviewed = sorted(used - reviewed)
    recs = Counter(data["decision"]["value"] for _, data, _ in vr)

    # AI systems
    ais = of("ais")
    tiers = Counter(x.get("tier_name", "unknown") for _, _, x in ais)
    aiia_systems = {data.get("system") for _, data, _ in of("aiia")}
    live_t1_no_aiia = [rel for rel, data, x in ais if x.get("tier") in ("0", "1") and data["lifecycle"] == "live"
                       and data["id"] not in aiia_systems]

    # Controls
    ctl = of("ctl")
    ctl_op = Counter(data["operating"] for _, data, _ in ctl if data["lifecycle"] == "in-use")

    # Regulatory change
    rc_open = [(md.get("due", ""), md.get("id", rel), md.get("title", ""), rel) for rel, md in docs
               if md.get("type") == "regulatory-change" and is_open(md.get("status"))]
    scanned = len(records) + len(docs)

    def files(lst, n=8):
        lst = list(lst)
        s = ", ".join(f"`{x}`" for x in lst[:n])
        return s + (f", and {len(lst) - n} more" if len(lst) > n else "") if lst else "none"

    L = [
        "# Program metrics",
        "",
        f"Generated by `gov metrics` on {today.isoformat()} from `{a.root}`. "
        f"Reporting period: {since.isoformat()} to {today.isoformat()}. Counts reflect what the records say; "
        "a register that's incomplete undercounts. Don't edit by hand; fix the records and rebuild.",
        "",
        f"Records scanned: {scanned} ({len(records)} gov records, {len(docs)} other deliverables)",
        "",
        "## 1. Records by type and status",
        "",
        "| Type | Total | New this period | By status |",
        "|---|---|---|---|",
    ]
    for t in sorted(by_type):
        st = "; ".join(f"{k} {v}" for k, v in sorted(by_type_status[t].items()))
        L.append(f"| {t} | {by_type[t]} | {new_this_period[t]} | {st} |")

    L += ["", "## 2. Risk", "",
          f"Open risk register rows by current residual rating: High {risk_counts['High']}, Medium {risk_counts['Medium']}, Low {risk_counts['Low']}.",
          "", "### Open High current residual risks", "",
          "| Risk | Record | Description | File |", "|---|---|---|---|"]
    for rating, rid, doc_id, rel, desc in risks:
        if rating == "High":
            L.append(f"| {rid} | {doc_id} | {desc} | `{rel}` |")
    L += ["", "### Assessment-level current residual ratings", "",
          "| Record | Type | Current residual | Confirmed | Status | File |", "|---|---|---|---|---|---|"]
    for t, i, r, conf, stage, rel in sorted(assessed, key=lambda x: RATINGS.index(x[2])):
        L.append(f"| {i} | {t} | {r} | {'yes' if conf else 'no'} | {stage} | `{rel}` |")

    L += ["", "## 3. Overdue", "",
          f"Records past a review, test, or deadline date: {len(overdue)}. Actions past due: {len(actions_overdue)}. "
          f"Open launch blockers: {len(blockers_open)}.", "",
          "| Date | Item | What | File |", "|---|---|---|---|"]
    for d, i, k, rel in overdue:
        L.append(f"| {d} | {i} | {k} | `{rel}` |")
    for d, aid, doc_id, rel in sorted(actions_overdue):
        L.append(f"| {d} | {doc_id} {aid} | action due | `{rel}` |")
    if blockers_open:
        L += ["", "Open launch blockers:", "", "| Action | Record | Reason | File |", "|---|---|---|---|"]
        for aid, doc_id, b, rel in blockers_open:
            L.append(f"| {aid} | {doc_id} | {b} | `{rel}` |")

    avg = f"{sum(dsr_days) / len(dsr_days):.0f} days" if dsr_days else "n/a"
    L += ["", "## 4. Data subject requests", "",
          f"- Cases: {len(dsr)}. Responded on time: {len(dsr_on_time)}. Responded late: {len(dsr_late)}. "
          f"Open past deadline: {len(dsr_open_late)}. Average days to respond: {avg}.",
          f"- Late: {files(dsr_late)}",
          f"- Open past deadline: {files(dsr_open_late)}",
          f"- Cases without a responded date can't be timed: {sum(1 for _, data, _ in dsr if not data['responded'])}.",
          "- Timeliness is measured against the deadline gov computes for each case (`extended_deadline` if set, else the "
          "earliest substantive deadline for its regimes). Lateness is provisional until the regimes are confirmed.",
          f"- Internal target (cases with `internal_target`): met {len(sla_met)}, missed {len(sla_missed)}. "
          "Report separately from statutory timeliness.",
          "", "## 5. Incidents", "",
          f"- Records: {len(inc)}. Assessed as personal data breaches (provisional or confirmed): {len(inc_breach)}. Open: {len(inc_open)}.",
          f"- Breaches: {files(inc_breach)}",
          f"- Under privilege (report counts and status only): {files(rel for rel, data, _ in inc if data.get('privilege'))}",
          "", "## 6. Vendors", "",
          f"- Vendor reviews: {len(vr)}. Recommendations: " + ("; ".join(f"{k} {v}" for k, v in sorted(recs.items())) or "none") + ".",
          f"- Reviews: {files(rel for rel, _, _ in vr)}",
          f"- Vendors named in the RoPA without a vendor review: {len(unreviewed)} ({', '.join(unreviewed) or 'none'}).",
          "", "## 7. AI systems", "",
          f"- Inventory entries: {len(ais)}. By tier: " + ("; ".join(f"{k} {v}" for k, v in sorted(tiers.items())) or "none") + ".",
          f"- Live Tier 0 or Tier 1 systems without an AI impact assessment: {len(live_t1_no_aiia)} ({files(live_t1_no_aiia)}).",
          "", "## 8. Controls", "",
          f"- Controls: {len(ctl)}. In use, by operating status: " + ("; ".join(f"{k} {v}" for k, v in sorted(ctl_op.items())) or "none") + ".",
          "", "## 9. Open regulatory changes", "",
          "| Due | Item | Title | File |", "|---|---|---|---|"]
    for due, i, t, rel in sorted(rc_open):
        L.append(f"| {due} | {i} | {t} | `{rel}` |")
    L.append("")

    out = a.out or os.path.join(a.root, "reports", f"metrics-{today.isoformat()}.md")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"Wrote {out}: {scanned} records, {risk_counts['High']} open High risks, {len(overdue)} overdue records, "
          f"{len(actions_overdue)} overdue actions, {len(dsr_late) + len(dsr_open_late)} late DSRs.")

