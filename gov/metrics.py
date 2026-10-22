"""Count the program's key metrics from deliverable metadata and registers.

Usage:
  gov metrics <output-root> --as-of YYYY-MM-DD [--since YYYY-MM-DD] [--out FILE]

Scans every *.md file under the output root (default compliance/), reads
each file's metadata block and its risk register and action plan tables,
and writes <output-root>/reports/metrics-YYYY-MM-DD.md (or --out). Every
number lists the files it was counted from, so each figure in a leadership
report can be traced to a record. --since sets the start of the reporting
period (default 90 days before --as-of) for "new this period" counts.

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
    d = DATE.search(v or "")
    return dt.date.fromisoformat(d.group(1)) if d else None


def first_rating(cell):
    for r in RATINGS:
        if re.search(r"\b" + r + r"\b", cell):
            return r
    return None


def tables(text):
    """Yield (header cells, rows of cells) for each Markdown table."""
    block = []
    for line in text.split("\n") + [""]:
        if line.startswith("|"):
            block.append([c.strip() for c in line.strip().strip("|").split("|")])
        else:
            if len(block) >= 3 and set("".join(block[1])) <= set("-: "):
                yield [h.lower() for h in block[0]], block[2:]
            block = []


def col(header, *names):
    for i, h in enumerate(header):
        if any(n in h for n in names):
            return i
    return None


def is_open(status):
    return not any(c in (status or "").lower() for c in CLOSED)


def main(argv=None):
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

    docs = []
    for dirpath, _, names in os.walk(a.root):
        if os.path.basename(dirpath) == "reports":
            continue
        for n in sorted(names):
            if not n.endswith(".md") or n in SKIP or n.endswith(("-notices.md", "-drafts.md")):
                continue
            p = os.path.join(dirpath, n)
            try:
                text = open(p, encoding="utf-8").read()
            except (OSError, UnicodeDecodeError):
                continue
            md = meta(text)
            if md is None:
                continue
            docs.append((os.path.relpath(p, a.root), md, text))

    src = defaultdict(list)  # metric -> files
    by_type = Counter()
    by_type_status = defaultdict(Counter)
    new_this_period = Counter()
    for rel, md, _ in docs:
        t = md.get("type", "unknown")
        by_type[t] += 1
        by_type_status[t][md.get("status", "unknown")] += 1
        started = date_of(md.get("date_prepared") or md.get("received") or md.get("aware_at"))
        if started and since <= started <= today:
            new_this_period[t] += 1

    # Overdue dates on open records
    overdue = []
    for rel, md, _ in docs:
        if not is_open(md.get("status")):
            continue
        for k in ("next_review", "next_test", "earliest_deadline", "due"):
            d = date_of(md.get(k))
            if d and d < today:
                overdue.append((d, md.get("id", rel), k.replace("_", " "), rel))
    overdue.sort()

    # Risks and actions from tables
    risks = []  # (rating, id, doc id, rel, text)
    actions_overdue = []
    blockers_open = []
    for rel, md, text in docs:
        doc_id = md.get("id", rel)
        doc_open = is_open(md.get("status"))
        for header, rows in tables(text):
            ci = col(header, "current residual")
            if ci is not None and header and header[0] == "id":
                for r in rows:
                    if len(r) > ci and re.match(r"R\d+$", r[0]):
                        rating = first_rating(r[ci])
                        if rating and doc_open:
                            risks.append((rating, r[0], doc_id, rel, r[1][:90] if len(r) > 1 else ""))
            di, si, bi = col(header, "due"), col(header, "status"), col(header, "launch blocker")
            if di is not None and si is not None and header and header[0] == "id":
                for r in rows:
                    if len(r) <= max(di, si) or not re.match(r"A\d+$", r[0]) or not is_open(r[si]):
                        continue
                    d = date_of(r[di])
                    if d and d < today:
                        actions_overdue.append((d, r[0], doc_id, rel))
                    if bi is not None and len(r) > bi and r[bi].lower().startswith("yes"):
                        blockers_open.append((r[0], doc_id, r[bi], rel))
    risk_counts = Counter(r[0] for r in risks)

    # Assessment-level residual ratings
    assessed = []
    for rel, md, _ in docs:
        rr = md.get("residual_risk", "")
        m = re.search(r"current:\s*([A-Za-z]+)", rr)
        if m and m.group(1) in RATINGS:
            assessed.append((md.get("type"), md.get("id", rel), m.group(1), "confirmed: true" in rr, md.get("stage", ""), rel))

    # DSRs
    dsr = [(rel, md) for rel, md, _ in docs if md.get("type") == "dsr"]
    dsr_on_time, dsr_late, dsr_open_late, dsr_days = [], [], [], []
    sla_met, sla_missed = [], []
    for rel, md in dsr:
        rec, resp = date_of(md.get("received")), date_of(md.get("responded"))
        # Statutory deadline: the extended date if an extension went out, else the earliest deadline.
        dl = date_of(md.get("extended_deadline")) or date_of(md.get("earliest_deadline"))
        target = date_of(md.get("internal_target"))
        if resp and dl:
            (dsr_on_time if resp <= dl else dsr_late).append(rel)
            if rec:
                dsr_days.append((resp - rec).days)
        elif not resp and dl and dl < today and is_open(md.get("status")):
            dsr_open_late.append(rel)
        if target and (resp or target < today):
            (sla_met if resp and resp <= target else sla_missed).append(rel)

    # Incidents
    inc = [(rel, md) for rel, md, _ in docs if md.get("type") in ("incident", "inc")]
    inc_breach = [rel for rel, md in inc if md.get("personal_data_breach", "").lower().startswith("yes")]
    inc_open = [rel for rel, md in inc if is_open(md.get("status"))]

    # Vendors
    vr = [(rel, md) for rel, md, _ in docs if md.get("type") in ("vendor-review", "vr")]
    # Vendor reviews as gov records name their vendor in vendor_slug; older Markdown reviews sit in vendors/<slug>/.
    reviewed = {md["vendor_slug"] for _, md in vr if md.get("vendor_slug")}
    reviewed |= {rel.split(os.sep)[1] for rel, md in vr if not md.get("vendor_slug") and rel.startswith("vendors" + os.sep) and rel.count(os.sep) >= 2}
    used = set()
    for rel, md, _ in docs:
        if md.get("type") == "ropa":
            used.update(s.strip() for s in md.get("vendors", "").strip("[]").split(",") if s.strip() and "<" not in s)
    unreviewed = sorted(used - reviewed)
    recs = Counter(re.sub(r"\s*\(.*\)$", "", md.get("recommendation", "none")) for _, md in vr)

    # AI systems
    ais = [(rel, md) for rel, md, _ in docs if md.get("type") == "ai-system"]
    tiers = Counter((md.get("tier", "unknown").split("(")[0].strip() or "unknown") for _, md in ais)
    aiia_systems = {md.get("system") for _, md, _ in docs if md.get("type") == "ai-impact-assessment"}
    live_t1_no_aiia = [rel for rel, md in ais if md.get("tier", "").startswith("1") and md.get("lifecycle", "").startswith("live")
                       and md.get("id") not in aiia_systems]

    # Controls
    ctl = [(rel, md) for rel, md, _ in docs if md.get("type") == "control"]
    ctl_op = Counter(md.get("operating", "unknown") for _, md in ctl)

    # Regulatory change
    rc_open = [(md.get("due", ""), md.get("id", rel), md.get("title", ""), rel) for rel, md, _ in docs
               if md.get("type") == "regulatory-change" and is_open(md.get("status"))]

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
        f"Records scanned: {len(docs)}",
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
          "| Record | Type | Current residual | Confirmed | Stage | File |", "|---|---|---|---|---|---|"]
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
        L += ["", "Open launch blockers:", "", "| Action | Record | Blocker | File |", "|---|---|---|---|"]
        for aid, doc_id, b, rel in blockers_open:
            L.append(f"| {aid} | {doc_id} | {b} | `{rel}` |")

    avg = f"{sum(dsr_days) / len(dsr_days):.0f} days" if dsr_days else "n/a"
    L += ["", "## 4. Data subject requests", "",
          f"- Cases: {len(dsr)}. Responded on time: {len(dsr_on_time)}. Responded late: {len(dsr_late)}. "
          f"Open past deadline: {len(dsr_open_late)}. Average days to respond: {avg}.",
          f"- Late: {files(dsr_late)}",
          f"- Open past deadline: {files(dsr_open_late)}",
          f"- Cases without a responded date can't be timed: {sum(1 for _, md in dsr if not date_of(md.get('responded')))}.",
          "- Timeliness is measured against each case's recorded statutory deadline (`extended_deadline` if set, else "
          "`earliest_deadline`). Lateness is provisional until the deadline is confirmed for the laws and request type.",
          f"- Internal target (cases with `internal_target`): met {len(sla_met)}, missed {len(sla_missed)}. "
          "Report separately from statutory timeliness.",
          "", "## 5. Incidents", "",
          f"- Records: {len(inc)}. Assessed as personal data breaches (provisional or confirmed): {len(inc_breach)}. Open: {len(inc_open)}.",
          f"- Breaches: {files(inc_breach)}",
          "", "## 6. Vendors", "",
          f"- Vendor reviews: {len(vr)}. Recommendations: " + ("; ".join(f"{k} {v}" for k, v in sorted(recs.items())) or "none") + ".",
          f"- Vendors named in the RoPA without a review folder: {len(unreviewed)} ({', '.join(unreviewed) or 'none'}).",
          "", "## 7. AI systems", "",
          f"- Inventory entries: {len(ais)}. By tier: " + ("; ".join(f"{k} {v}" for k, v in sorted(tiers.items())) or "none") + ".",
          f"- Live Tier 1 systems without an AI impact assessment: {len(live_t1_no_aiia)} ({files(live_t1_no_aiia)}).",
          "", "## 8. Controls", "",
          f"- Controls: {len(ctl)}. By operating status: " + ("; ".join(f"{k} {v}" for k, v in sorted(ctl_op.items())) or "none") + ".",
          "", "## 9. Open regulatory changes", "",
          "| Due | Item | Title | File |", "|---|---|---|---|"]
    for due, i, t, rel in sorted(rc_open):
        L.append(f"| {due} | {i} | {t} | `{rel}` |")
    L.append("")

    out = a.out or os.path.join(a.root, "reports", f"metrics-{today.isoformat()}.md")
    os.makedirs(os.path.dirname(out) or ".", exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(L))
    print(f"Wrote {out}: {len(docs)} records, {risk_counts['High']} open High risks, {len(overdue)} overdue records, "
          f"{len(actions_overdue)} overdue actions, {len(dsr_late) + len(dsr_open_late)} late DSRs.")

