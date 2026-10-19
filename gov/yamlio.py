"""YAML loading that keeps dates as strings, so records round-trip exactly."""
from __future__ import annotations

import yaml


class Loader(yaml.SafeLoader):
    pass


# Dates stay strings ("2026-10-18"), matching the schemas' date patterns.
Loader.yaml_implicit_resolvers = {
    key: [(tag, rx) for tag, rx in resolvers if tag != "tag:yaml.org,2002:timestamp"]
    for key, resolvers in yaml.SafeLoader.yaml_implicit_resolvers.items()
}


def loads(text: str):
    return yaml.load(text, Loader=Loader)


def load(path):
    with open(path, encoding="utf-8") as f:
        return loads(f.read())


def dumps(data) -> str:
    return yaml.safe_dump(data, sort_keys=False, allow_unicode=True, default_flow_style=False, width=1000)
