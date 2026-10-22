"""Rebuild the leadership-report eval fixtures as gov records.

Usage: python build_fixtures.py <scratch folder>, then copy <scratch folder>/compliance over evals/files/compliance.
Regulatory change memos and past reports are copied from the current fixtures; gov doesn't manage them yet.
"""
import shutil, sys
from pathlib import Path
from gov import yamlio
from gov.skeleton import new_record
from gov.render import render_tree
from gov.validate import validate_tree

REPO = Path(__file__).resolve().parents[3]
root = Path(sys.argv[1])
shutil.rmtree(root, ignore_errors=True)
(root / "skills").mkdir(parents=True)
shutil.copytree(REPO / "skills/_shared", root / "skills/_shared")
comp = root / "compliance"
counters = {}

def set_counter(key, n):
    counters[key] = n
    (comp / ".gov").mkdir(parents=True, exist_ok=True)
    (comp / ".gov/counters.yaml").write_text(yamlio.dumps({"version": 1, "counters": counters}), encoding="utf-8")

def make(rtype, key, number, slug, title, date, change):
    set_counter(key, number - 1)
    path = new_record(root, rtype, slug, title, date, "Claude (privacy-governance suite)")
    counters.update(yamlio.load(comp / ".gov/counters.yaml")["counters"])
    data = yamlio.load(path)
    change(data)
    path.write_text(yamlio.dumps(data), encoding="utf-8")
    return path

P = lambda v, r="Recorded for the eval fixture": {"value": v, "status": "Provisional", "reason": r}
C = lambda v, r="Recorded for the eval fixture": {"value": v, "status": "Confirmed", "reason": r}
lvl = lambda l, s: {"likelihood": l, "severity": s}
def act(i, text, owner, due, blocking=False, reason=None, scope=None, status="open"):
    a = {"id": i, "action": text, "owner": owner, "due": due, "closure_evidence": "Evidence on file", "launch_blocking": blocking, "status": status}
    if blocking:
        a["block_reason"] = reason
        if scope:
            a["scope"] = scope
    return a

# DSRs
for n, (recv, resp, status) in enumerate([("2026-07-03", "2026-07-28", "Closed"), ("2026-07-20", "2026-09-02", "Closed"),
                                          ("2026-08-25", "2026-09-20", "Closed"), ("2026-09-10", None, "In progress"),
                                          ("2026-10-05", None, "Awaiting verification")], start=1):
    def dsr(d, resp=resp, status=status):
        d.update(status=status, request_types=["access"], roles=[{"data": "Customer account", "role": C("controller")}], regimes=["gdpr", "ccpa"],
                 requester_type="data-subject", requester_words="Please send me a copy of my data.",
                 responded=resp, closed=resp if status == "Closed" else None,
                 laws=[{"law": "GDPR", "applies": P(True)}, {"law": "CCPA", "applies": P(True)}],
                 summary="Access request from a customer.", analysis="Fixture case for the leadership report eval.")
        d["received"].update(time="10:00 ET", channel="Privacy inbox")
        d["verification"].update(method="Email on file", why="Matches the account", status="verified" if resp else "requested",
                                 by="Support lead" if resp else None, date=resp)
        if resp:
            d["messages"] = [{"message": "response", "to": "Requester", "text": "Your data is attached.", "approved_by": "Privacy lead", "sent": resp, "sent_by": "Support lead"}]
    make("dsr", "DSR-2026", n, f"access-{n}", "Access, customer", recv, dsr)

# AI inventory
def ais(lifecycle, tier, review, title):
    def f(d):
        d.update(status="Draft", lifecycle=lifecycle, tier=C(tier), next_review=review, source="vendor-product",
                 summary=f"{title}.", analysis="Fixture entry for the leadership report eval.", decision=C("proceed-to-follow-ons"))
    return f
make("ais", "AIS", 3, "talentrank", "TalentRank", "2026-09-01", ais("pilot", "1", "2027-03-01", "TalentRank resume screening"))
make("ais", "AIS", 4, "support-copilot", "Support copilot", "2026-05-10", ais("live", "1", "2026-11-10", "Support copilot"))
make("ais", "AIS", 5, "code-assistant", "Engineering code assistant", "2026-02-10", ais("live", "3", "2027-02-10", "Engineering code assistant"))

# Controls
set_counter("EV", 1)
def ctl(operating, next_test, cco, evidence=None):
    def f(d):
        d.update(status="Draft", operating=operating, next_test=next_test, design="implemented" if operating != "planned" else "designed",
                 frequency="quarterly", test_frequency="annual", owner="Control owner", systems="Production", description="Fixture control for the leadership report eval.", source="Team notes")
        d["objectives"] = [{"cco": cco, "how": "Fixture mapping", "coverage": "none-yet" if operating == "planned" else "partial", "not_satisfied": "none"}]
        if evidence:
            d["evidence"] = [evidence]
    return f
make("ctl", "CTL", 1, "admin-access-review", "Quarterly admin access review", "2026-03-01",
     ctl("evidenced", "2026-12-31", "CCO-15", {"id": "EV-0001", "status": "on-file", "type": "record", "shows": "operation", "what": "Q3 review ticket",
                                              "location": "https://tickets.example/IT-1", "date": "2026-09-30", "period": "Q3 2026", "owner": "IT lead", "stale_after": "2027-01-01"}))
make("ctl", "CTL", 2, "dsr-intake-form", "DSR intake form", "2026-03-01", ctl("unverified", "2026-09-30", "CCO-09"))
make("ctl", "CTL", 3, "ai-red-team", "AI red-team testing every 3 months", "2026-03-01", ctl("planned", "2026-11-15", "CCO-30"))

# RoPA: from the test fixture, with each entry's vendors as processors
base = yamlio.load(REPO / "tests/fixtures/ropa/ROPA-0001-gradebook-sync.yaml")
def ropa(title, prepared, review, vendors):
    def f(d):
        keep = {k: base[k] for k in base if k not in ("id", "title", "date_prepared", "next_review", "version_history", "signoff", "status")}
        d.update(keep)
        d.update(status="Draft", date_prepared=prepared, next_review=review, actions=[])
        proto = next(r for r in base["recipients"] if isinstance(r, dict))
        d["recipients"] = [dict(proto, name=v.replace("-", " ").title(), kind="processor", vendor=v, vendor_review="recommended") for v in vendors]
        d["related"]["vendor_reviews"] = [] if "vendor_reviews" in d.get("related", {}) else d["related"].get("vendor_reviews", [])
    return f
make("ropa", "ROPA", 1, "gradebook-sync", "Gradebook sync", "2026-03-01", ropa("Gradebook sync", "2026-03-01", "2027-03-01", ["lumen-analytics", "cloudhost"]))
make("ropa", "ROPA", 2, "recruiting", "Recruiting", "2025-06-01", ropa("Recruiting", "2025-06-01", "2026-06-01", ["talentrank", "greenhouse"]))

# DPIAs
def dpia(status, review, risks, actions, decision):
    def f(d):
        d.update(status=status, next_review=review, risks=risks, actions=actions, decision=decision,
                 summary="Fixture DPIA for the leadership report eval.", analysis="Fixture analysis.")
    return f
make("dpia", "DPIA-2026", 2, "support-call-recording", "Support call recording and transcription", "2026-04-02",
     dpia("Draft", "2026-10-01", [{"id": "R1", "risk": "Callers not told about recording in two-party consent states", "inherent": lvl("probable", "significant"),
          "current": lvl("remote", "significant"), "target": lvl("remote", "significant"), "measures": [{"measure": "IVR notice", "status": "verified", "evidence": "IVR recording"}], "owner": "Support Ops"}],
          [], C("proceed")))
make("dpia", "DPIA-2026", 4, "gradebook-sync", "Gradebook sync with district SIS", "2026-08-12",
     dpia("In review", "2027-08-12", [
         {"id": "R1", "risk": "Students' deleted records are recreated by the nightly roster sync, so deletion requests fail", "inherent": lvl("probable", "significant"),
          "current": lvl("probable", "significant"), "target": lvl("remote", "significant"), "measures": [{"measure": "Honor deletion tombstones", "status": "planned", "evidence": "A1"}], "owner": "Integrations"},
         {"id": "R2", "risk": "Teachers' grade comments exposed to other districts through a shared tenant", "inherent": lvl("possible", "severe"),
          "current": lvl("possible", "significant"), "target": lvl("remote", "severe"), "measures": [{"measure": "Tenant isolation (SOC 2)", "status": "verified", "evidence": "SOC 2 report"}, {"measure": "Pen test", "status": "planned", "evidence": "A2"}], "owner": "Security"}],
         [act("A1", "Honor deletion tombstones in roster sync", "Integrations", "2026-09-30", True, "law", "GDPR Art. 17"),
          act("A2", "Tenant isolation pen test", "Security", "2026-11-30", True, "risk")], P("proceed-with-conditions")))

# AI impact assessment
def aiia(d):
    d.update(system="AIS-0003", tier="1", summary="TalentRank resume screening.", analysis="Fixture assessment.",
             risks=[{"id": "R1", "risk": "Candidates screened out by a model with no bias testing on the company's applicant pool", "inherent": lvl("probable", "severe"),
                     "current": lvl("probable", "severe"), "target": lvl("possible", "significant"), "measures": [{"measure": "Bias testing", "status": "planned", "evidence": "A1"}], "owner": "People Analytics"}],
             actions=[act("A1", "Commission bias testing", "People Analytics", "2026-10-31", True, "law", "NYC Admin. Code § 20-871")])
make("aiia", "AIIA-2026", 1, "talentrank", "TalentRank resume screening", "2026-09-20", aiia)

# Vendor reviews
def vr(status, decision, risks, actions):
    def f(d):
        d.update(status=status, decision=decision, risks=risks, actions=actions, summary="Fixture vendor review.", analysis="Fixture analysis.")
    return f
make("vr", "VR-2026", 7, "lumen-analytics", "Lumen Analytics: product analytics", "2026-07-15",
     vr("Draft", C("approve-with-conditions"), [{"id": "R1", "risk": "Transfers to the US without SCCs", "inherent": lvl("possible", "significant"),
        "current": lvl("possible", "significant"), "target": lvl("remote", "significant"), "measures": [{"measure": "SCCs Module 2", "status": "planned", "evidence": "A1"}], "owner": "Procurement"}],
        [act("A1", "Vendor signs SCCs Module 2", "Procurement", "2026-09-15")]))
make("vr", "VR-2026", 9, "scribe-ai", "ScribeAI: meeting transcription", "2026-10-02",
     vr("Draft", P("do-not-approve"), [{"id": "R1", "risk": "Meeting audio used to train the vendor's models without a contract limit", "inherent": lvl("probable", "severe"),
        "current": lvl("probable", "severe"), "target": lvl("possible", "significant"), "measures": [{"measure": "Training opt-out", "status": "absent", "evidence": "Contract change"}], "owner": "Procurement"}], []))

# Incidents
def inc(status, aware, states, breach, closed=False, privilege=None):
    def f(d):
        d.update(privilege=privilege, status=status, states=states, breach=breach, summary="Fixture incident.", analysis="Fixture analysis.", commander="Security lead")
        d["awareness"].update(time=aware, tz="America/New_York", reasoning="Fixture", confirmed=True)
        if closed:
            d["closure"].update(closed=closed, root_cause="Autocomplete picked the wrong parent's address", follow_ons="Recipient check before sending")
    return f
make("inc", "INC-2026", 3, "misdirected-email", "Report card emailed to wrong parent", "2026-08-14",
     inc("Draft", "2026-08-14T09:10", ["NY"], P(True, "A student's report card reached the wrong parent"), closed="2026-08-20"))
make("inc", "INC-2026", 4, "s3-bucket", "Misconfigured storage bucket", "2026-09-28",
     inc("In review", "2026-09-28T16:00", ["CA", "NY"], P("TBC", "Access logs not yet reviewed"), privilege="Privileged and confidential, prepared at the direction of counsel (J. Ortiz)"))

old = REPO / "skills/leadership-report/evals/files/compliance"
for sub in ("regulatory-change", "reports"):
    shutil.copytree(old / sub, comp / sub)
problems = [p for p in validate_tree(root) if p.level == "error"]
for p in problems:
    print(p)
if not problems:
    print(render_tree(root).written[:3], "...")
