#!/usr/bin/env python3
"""Gate 7: model artifact contract (CR-IM-CAT-03).

Validates every model artifact at models/**/*.yaml against the contract in
docs/RECORD-STANDARD.md section 4, and the two-way binding between artifact
and record:

  - artifact shape: model, record, title, model_form (enum), model_scope,
    represents (canonical Business Object id form), attributes[] (name, type,
    cardinality, definition), sources[] (kind + reference)
  - the referenced record exists as a canonical record file
  - that record's evidence cites the artifact path (repository-path)
"""

from __future__ import annotations

import glob
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
MODEL_GLOB = "models/**/*.yaml"
RECORD_GLOB = "entities/v1-alpha/**/*.yaml"
FORM_ENUM = {"conceptual", "logical", "schema", "ontology", "other"}
BO_ID = re.compile(r"^objects:object-[a-z0-9-]+$")
REQUIRED_ATTR_KEYS = {"name", "type", "cardinality", "definition"}
SOURCE_KINDS = {"repository-path", "system-of-record", "published-document"}


def main() -> int:
    findings: list[str] = []

    artifacts = sorted(glob.glob(str(REPO / MODEL_GLOB), recursive=True))
    records: dict[str, dict] = {}
    for f in glob.glob(str(REPO / RECORD_GLOB), recursive=True):
        if "/research/" in f or "/candidates/" in f or "/retired/" in f:
            continue
        doc = yaml.safe_load(Path(f).read_text(encoding="utf-8")) or {}
        if doc.get("id"):
            records[doc["id"]] = {"doc": doc, "path": Path(f)}

    print(f"Model artifacts: {len(artifacts)}; canonical records: {len(records)}")

    for path in artifacts:
        rel = Path(path).relative_to(REPO)
        doc = yaml.safe_load(Path(path).read_text(encoding="utf-8")) or {}

        for key in ("model", "record", "title", "model_form", "model_scope", "represents", "attributes", "sources"):
            if key not in doc:
                findings.append(f"{rel}: missing required key '{key}'")
        if findings and len(findings) >= 8:
            break

        if doc.get("model_form") not in FORM_ENUM:
            findings.append(f"{rel}: model_form {doc.get('model_form')!r} not in {sorted(FORM_ENUM)}")
        if not BO_ID.match(str(doc.get("represents") or "")):
            findings.append(f"{rel}: represents {doc.get('represents')!r} is not a canonical Business Object id")

        attrs = doc.get("attributes") or []
        if not isinstance(attrs, list) or len(attrs) < 1:
            findings.append(f"{rel}: attributes must be a non-empty list")
        else:
            for a in attrs:
                missing = REQUIRED_ATTR_KEYS - set(a or {})
                if missing:
                    findings.append(f"{rel}: attribute {a.get('name', '?')!r} missing {sorted(missing)}")

        for s in doc.get("sources") or []:
            if s.get("kind") not in SOURCE_KINDS:
                findings.append(f"{rel}: source kind {s.get('kind')!r} not known")

        # two-way binding: artifact.record exists, and that record cites this artifact
        rid = doc.get("record")
        if rid and rid in records:
            ev = (records[rid]["doc"].get("evidence") or {}).get("sources") or []
            cited = any(str(s.get("reference", "")).endswith(str(rel)) for s in ev)
            if not cited:
                findings.append(
                    f"{rel}: record {rid} does not cite this artifact in its evidence sources"
                )
        elif rid:
            findings.append(f"{rel}: record {rid!r} not found in canonical records")

    if findings:
        for f in findings:
            print(f"FAIL: {f}")
        print(f"Findings: {len(findings)}")
        return 1

    print("OK: model artifacts conform to the CR-IM-CAT-03 contract (two-way binding verified)")
    print("Findings: 0")
    return 0


if __name__ == "__main__":
    sys.exit(main())
