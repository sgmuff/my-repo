"""The `gov` command."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

from gov import __version__, ids, yamlio
from gov.paths import RootNotFound, find_root
from gov.render import render_tree
from gov.route import RoutingError, questions_markdown, route, to_markdown
from gov.skeleton import SkeletonError, new_record
from gov.validate import validate_tree


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(prog="gov", description="Records, routing, validation, and rendering for the governance suite.")
    parser.add_argument("--root", help="repository root (default: GOV_ROOT, or the nearest parent holding the suite)")
    parser.add_argument("--version", action="version", version=f"gov {__version__}")
    sub = parser.add_subparsers(dest="command", required=True)

    p = sub.add_parser("next-id", help="reserve the next ID for a prefix")
    p.add_argument("prefix")
    p.add_argument("--year", help="YYYY, for prefixes that carry a year")

    p = sub.add_parser("new", help="create a record skeleton with a fresh ID")
    p.add_argument("type")
    p.add_argument("--slug", required=True)
    p.add_argument("--title", required=True)
    p.add_argument("--date", required=True, help="date prepared, YYYY-MM-DD")
    p.add_argument("--prepared-by", default="Claude (privacy-governance suite)")

    p = sub.add_parser("validate", help="check every record")
    p.add_argument("--as-of", help="YYYY-MM-DD for the reference review check; defaults to each record's own date")

    p = sub.add_parser("render", help="write Markdown and indexes from the records")
    p.add_argument("--check", action="store_true", help="write nothing; fail if any output is stale")

    sub.add_parser("index", help="rebuild register indexes (same as render)")

    p = sub.add_parser("required", help="list the assessments a record or set of facts owes")
    p.add_argument("source", help="a record YAML file, or a facts YAML file, or - for stdin")
    p.add_argument("--as-of", help="YYYY-MM-DD; defaults to a record's date_prepared, and is required for facts")
    p.add_argument("--format", choices=["yaml", "markdown"], default="markdown")

    p = sub.add_parser("screen", help="list the DPIA screening indicators a RoPA record suggests, marked Provisional")
    p.add_argument("record", help="a RoPA record YAML file")
    p.add_argument("--format", choices=["yaml", "markdown"], default="markdown")

    p = sub.add_parser("route", help="print the triage plan for a facts file")
    p.add_argument("facts", help="YAML file of deciding facts, or - for stdin")
    p.add_argument("--format", choices=["yaml", "markdown", "questions"], default="yaml",
                   help="markdown: the plan and decision register; questions: open facts ranked for asking")

    args = parser.parse_args(argv)
    try:
        root = Path(args.root).resolve() if args.root else find_root()
        return COMMANDS[args.command](root, args)
    except (RootNotFound, ids.IdError, SkeletonError, RoutingError) as exc:
        print(f"gov: {exc}", file=sys.stderr)
        return 2


def _next_id(root, args) -> int:
    print(ids.next_id(root, args.prefix, args.year))
    return 0


def _new(root, args) -> int:
    path = new_record(root, args.type, args.slug, args.title, args.date, args.prepared_by)
    print(path.relative_to(root))
    return 0


def _validate(root, args) -> int:
    problems = validate_tree(root, args.as_of)
    for problem in problems:
        print(problem)
    count = {level: sum(1 for p in problems if p.level == level) for level in ("error", "finding", "warning")}
    print(f"{count['error']} errors, {count['finding']} findings, {count['warning']} warnings")
    if count["finding"]:
        print("Findings are legal consistency questions: resolve each in the record, or record why it doesn't apply.")
    errors = count["error"]
    return 1 if errors else 0


def _render(root, args) -> int:
    result = render_tree(root, check=getattr(args, "check", False))
    if result.problems:
        for problem in result.problems:
            print(problem)
        print("Not rendered: fix the errors above first.")
        return 1
    if result.stale:
        for path in result.stale:
            print(f"{path}: stale; run `gov render`")
        return 1
    for path in result.written:
        print(f"wrote {path}")
    if not result.written:
        print("Everything is up to date.")
    return 0


def _required(root, args) -> int:
    from gov import required as req
    text = sys.stdin.read() if args.source == "-" else Path(args.source).read_text(encoding="utf-8")
    data = yamlio.loads(text) or {}
    if not isinstance(data, dict):
        raise RoutingError("the file must be a mapping")
    if data.get("type") == "ropa":
        facts, as_of = req.facts_from_ropa(data), args.as_of or data["date_prepared"]
    elif data.get("type"):
        raise RoutingError(f"gov required reads a RoPA record or a facts file, not a {data['type']} record; run it on the RoPA entry this record belongs to")
    else:
        if not args.as_of:
            raise RoutingError("pass --as-of YYYY-MM-DD with a facts file")
        facts, as_of = data, args.as_of
    try:
        results = req.evaluate(facts, as_of, root)
    except req.CatalogError as exc:
        raise RoutingError(str(exc)) from None
    print(req.to_markdown(results) if args.format == "markdown" else yamlio.dumps(results), end="")
    return 0


def _route(root, args) -> int:
    text = sys.stdin.read() if args.facts == "-" else Path(args.facts).read_text(encoding="utf-8")
    facts = yamlio.loads(text) or {}
    if not isinstance(facts, dict):
        raise RoutingError("the facts file must be a mapping of fact: value")
    result = route(root, facts)
    if args.format == "markdown":
        print(to_markdown(result), end="")
    elif args.format == "questions":
        print(questions_markdown(result), end="")
    else:
        print(yamlio.dumps(result), end="")
    return 0


def _screen(root, args) -> int:
    from gov.screen import screen, to_markdown
    data = yamlio.load(Path(args.record))
    if not isinstance(data, dict) or data.get("type") != "ropa":
        print("gov: screen reads a RoPA record", file=sys.stderr)
        return 2
    result = screen(data)
    print(to_markdown(result) if args.format == "markdown" else yamlio.dumps(result), end="")
    return 0


COMMANDS = {"screen": _screen, "required": _required, "next-id": _next_id, "new": _new, "validate": _validate, "render": _render, "index": _render, "route": _route}

if __name__ == "__main__":
    raise SystemExit(main())
