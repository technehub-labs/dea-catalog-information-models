# Customer Information Model

> The conceptual information model of the Customer business object: the attributes, constraints, and relationships that specify customer information for the enterprise, independent of any single persistent structure or consuming form.

## Identity

| Field | Value |
|---|---|
| Id | `dea:information-model-customer` |
| Type | InformationModel |
| Model form | conceptual |
| Model scope | Customer domain |
| Version | 1.0.0 |
| Lifecycle status | active |

## Evidence

- system-of-record: `dea-catalog-business-objects` (canonical record objects:object-customer-2qvphc)
- repository-path: `models/customer.yaml`

Two-part evidence: the canonical Business Object record is the semantic authority; the committed artifact is the model itself. Corroboration: internal — the BO definition and the sibling models along the Agreement→Offering→Product→Service→Resource→Entity chain (CR-IM-CAT-05).

## Classification-or-relationships

- `represents` -> `objects:object-customer-2qvphc` — the model specifies the information structure of that business object.
- `dea:structures` assertions: deferred until a downstream DataEntity or InformationAsset is stood up shaped by this model (the target catalogs are populated; the assertion is made by the first consuming stand-up).

## Provenance

candidate -> corroborated -> reviewed -> canonical, all 2026-11-01, actor Emmanuel A. Otchere (see record `provenance.ladder_passage`).

## Governance

- functional_owner: Emmanuel A. Otchere
- steward: Emmanuel A. Otchere
- approval_status: approved (review_date 2026-11-01)
- established_by: CR-IM-CAT-04
