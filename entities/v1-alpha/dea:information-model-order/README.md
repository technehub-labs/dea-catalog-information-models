# Order Information Model

> The conceptual information model of the Order business object: the attributes, constraints, and lifecycle statuses that specify sales-order information for the enterprise, independent of any single persistent structure or consuming form.

## Identity

| Field | Value |
|---|---|
| Id | `dea:information-model-order` |
| Type | InformationModel |
| Model form | conceptual |
| Model scope | Sales-order domain |
| Version | 1.0.0 |
| Lifecycle status | active |

## Evidence

- system-of-record: `dea-catalog-business-objects` (canonical record objects:object-order-bpy4g4)
- published-document: TMF SID Product Order domain (ProductOrder); TMF622 Product Ordering API
- repository-path: `models/order.yaml`

Two-part evidence: the canonical Business Object record is the semantic authority; the committed artifact is the model itself.

## Classification-or-relationships

- `represents` -> `objects:object-order-bpy4g4` — the model specifies the information structure of that business object.
- `dea:structures` assertions: deferred until a downstream DataEntity or InformationAsset is stood up shaped by this model (the target catalogs are populated; the assertion is made by the first consuming stand-up).

## Provenance

candidate -> corroborated -> reviewed -> canonical, all 2026-11-01, actor Emmanuel A. Otchere (see record `provenance.ladder_passage`).

## Governance

- functional_owner: Emmanuel A. Otchere
- steward: Emmanuel A. Otchere
- approval_status: approved (review_date 2026-11-01)
- established_by: CR-IM-CAT-04
