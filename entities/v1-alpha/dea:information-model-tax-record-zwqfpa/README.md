# Tax Record Information Model

> The conceptual information model of the Tax Record business object: the attributes, lifecycle states, and classification that specify tax record information for the enterprise, per the canonical Business Object record. Model scope: Finance & Accounting domain.

## Identity

| Field | Value |
|---|---|
| Id | `dea:information-model-tax-record-zwqfpa` |
| Type | InformationModel |
| Model form | conceptual |
| Model scope | Finance & Accounting domain |
| Chain stage | financial |
| Version | 1.0.0 |
| Lifecycle status | active |

## Evidence

- system-of-record: `dea-catalog-business-objects` (canonical record objects:object-tax-record-zwqfpa)
- repository-path: `models/tax-record-zwqfpa.yaml`

Two-part evidence: the canonical Business Object record is the semantic authority; the committed artifact is the model itself.

## Classification-or-relationships

- `represents` -> `objects:object-tax-record-zwqfpa`
- `dea:structures` assertions: deferred until a downstream DataEntity or InformationAsset is stood up shaped by this model.

## Provenance

candidate -> corroborated -> reviewed -> canonical, all 2026-11-01, actor Emmanuel A. Otchere (see record `provenance.ladder_passage`).

## Governance

- functional_owner: Emmanuel A. Otchere
- steward: Emmanuel A. Otchere
- approval_status: approved (review_date 2026-11-01)
- established_by: CR-IM-CAT-05
