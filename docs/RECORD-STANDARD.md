# Record Documentation Standard (CR-IM-CAT-01)

Every canonical Information Model record must satisfy this standard. Gate 6
(`scripts/check_record_documentation.py`) enforces the machine-checkable
subset; steward review enforces the rest.

## 1. Record file

One record per subtree: `entities/v1-alpha/<id>/<id>.yaml`, where `<id>` is
the canonical id (`dea:information-model-<slug>`). Obligations beyond the schema:

1. `name` is the real name as consumers know it.
2. `description` states what the record is and its consuming purpose — not
   a restatement of the name.
3. `evidence.sources` cites at least one verifiable source; `rationale`
   says why it justifies admission.
4. `provenance.ladder_passage` records passage to canonical with quoted
   dates and authorship-bearing actors (AUT rules).
5. Relationship instances are asserted only against canonical targets, or
   the README carries an explicit `Deferred:` note.

## 2. YAML conventions

- Dates single-quoted so they stay strings.
- Apostrophes escaped (`''`) in single-quoted prose; double quotes when the
  prose contains a colon.

## 3. Per-record README

Sections: `# <Name>` + verbatim definition blockquote, `## Identity`,
`## Evidence`, `## Classification-or-relationships`, `## Provenance`,
`## Governance`. The definition blockquote must equal the record's
`description` verbatim (Gate 6 checks).

## 4. Model artifact contract (CR-IM-CAT-03)

A canonical InformationModel record carries its **model artifact** — the model content itself — committed in this repository at `models/<slug>.yaml`. The record and the artifact are a two-way bound pair, and the pair is the two-part evidence rule:

1. **Provenance source** — where the model's semantics came from: the canonical Business Object record (system-of-record), an external published standard (published-document), or a producing repository (repository-path).
2. **Canonical artifact** — the committed model file itself (repository-path evidence, diff-able, gate-checked).

Artifact shape (gate `scripts/check_model_artifact.py`, Gate 7):

```yaml
model: customer                      # slug; file is models/<model>.yaml
record: dea:information-model-customer  # the canonical record this artifact belongs to
title: Customer Information Model
model_form: conceptual               # conceptual | logical | schema | ontology | other
model_scope: Customer domain
represents: objects:object-customer-2qvphc   # canonical Business Object id
attributes:
  - name: customerId
    type: identifier
    cardinality: 1..1
    definition: ...
constraints:
  - ...
sources:
  - kind: system-of-record           # same kinds as record evidence
    reference: ...
```

Rules: every attribute carries name, type, cardinality, and a one-sentence definition; `represents` must be a canonical Business Object id; the artifact's `record` must exist and that record's evidence must cite the artifact path. Diagrams are external references, never the canonical artifact (not diff-able, not gate-checkable).

## 5. Change discipline

Record changes land through CRs; a record edit regenerates `CATALOG.yaml`
in the same PR. Retired records move to `retired/`, never deleted.
