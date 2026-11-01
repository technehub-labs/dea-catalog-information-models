# CR-IM-CAT-04: Pilot Tranche — Three Business-Object Models

| Field | Value |
|---|---|
| **CR** | CR-IM-CAT-04 |
| **Title** | Pilot tranche: Customer, Invoice, and Order information models (first canonical records) |
| **Status** | Landed |
| **Layer** | Catalogue (L4 Information & Knowledge) |
| **Programme** | Information Model governance chain |
| **Repository** | `technehub-labs/dea-catalog-information-models` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-11-01 |
| **Depends on** | CR-IM-CAT-01, CR-IM-CAT-02, CR-IM-CAT-03 |
| **Trigger** | First execution of the CR-IM-CAT-03 evidence-input contract: the pilot proves the model-artifact format, the two-part evidence, and the TMF-anchoring step on real content before batching the remaining ~70 business objects. |

## 1. Executive summary

Three canonical InformationModel records admitted, each authored under the CR-IM-CAT-03 contract: **Customer** (Customer domain), **Invoice** (Billing domain), **Order** (Sales-order domain). Each is a conceptual-form model artifact committed at `models/<slug>.yaml` with a full attribute dictionary (name, type, cardinality, definition), constraints, a `represents` assertion onto the canonical Business Object id, and two-part evidence (canonical BO record as system-of-record + TMF published authority + the committed artifact). These are the first `dea:InformationModel` records in the ecosystem and the first assertions of `represents` from the model side.

## 2. The three models

| Record | Scope | Business Object | TMF anchor | Attributes |
|---|---|---|---|---|
| `dea:information-model-customer` | Customer domain | `objects:object-customer-2qvphc` | TMF SID Customer domain; TMF629 | 7 |
| `dea:information-model-invoice` | Billing domain | `objects:object-invoice-z3fwgb` | TMF SID Billing domain; TMF678 | 8 |
| `dea:information-model-order` | Sales-order domain | `objects:object-order-bpy4g4` | TMF SID Product Order domain; TMF622 | 7 |

## 3. Evidence

Two-part per the CR-IM-CAT-03 contract: provenance (canonical BO record + TMF published authority) and the committed artifact. The corroborated ladder stage records the TMF-anchoring check. `dea:structures` assertions are deliberately deferred — they fire when a downstream DataEntity or InformationAsset is stood up shaped by one of these models.

## 4. Acceptance criteria

1. All gates Findings: 0 (including Gate 7 with 3 artifacts + two-way bindings).
2. CATALOG.yaml: 3 canonical records.
3. Every record's `represents` target verified against the live business-objects CATALOG.yaml.

## 5. NOT-list

1. No `dea:structures` assertions yet (deferred by design).
2. No logical-form models yet (the pilot is conceptual; logical forms mature with persistence work).
3. No further BOs modeled in this CR (batching follows in domain-family tranches).
