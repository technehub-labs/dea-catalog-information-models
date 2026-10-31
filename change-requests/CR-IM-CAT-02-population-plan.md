# CR-IM-CAT-02: Population Plan (Zero Records)

| Field | Value |
|---|---|
| **CR** | CR-IM-CAT-02 |
| **Title** | Population plan: candidate sources named, admission evidence-gated (zero records) |
| **Status** | Landed |
| **Layer** | Catalogue (L4 Information & Knowledge) |
| **Programme** | Information Model governance chain |
| **Repository** | `technehub-labs/dea-catalog-information-models` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-11-01 |
| **Depends on** | CR-IM-CAT-01 (kit) |
| **Trigger** | The evidence-only admission rule (FOUNDATIONS D-5): no org-verifiable information-model artifact exists in the repositories today, so the catalogue lands its plan and admits nothing. |

## 1. Executive summary

This CR records the population plan and admits **zero records**. The catalogue's purpose — holding the enterprise's conceptual/logical information models — is served the moment the first verifiable model artifact exists; this CR names where those will come from and what admission will require.

## 2. Candidate sources (named, not admitted)

1. **The domain-ontology pillar**: `dea-catalog-ontologies` (fintech, healthcare OWL) — scaffold today; its first ontology is a canonical InformationModel candidate (model_form: ontology).
2. **Business-object attribute models**: models specifying the structure of the 74 canonical business objects (Customer, Order, Invoice) — the U-1 follow-on once the business-objects catalog publishes attribute-level structure.
3. **ESA/EO artifacts**: the Enterprise Semantic Architecture and Enterprise Ontology pillars (both scaffolds) — their first formal vocabularies/schema artifacts.
4. **Integration-interface payload schemas**: when api-contracts/integration-interfaces publish payload models.

## 3. Admission requirements (per FOUNDATIONS)

Each candidate must: cite the producing artifact (repository path or system of record); declare `model_form`; pass the boundary test — a model **specifies** structure (via dea:structures onto DataEntity/InformationAsset), it is not itself a class (maps-to target), a consumable form, or a persistent structure.

## 4. Scope

In scope: FOUNDATIONS section 7 population plan; this CR; register row; CHANGELOG.

Out of scope: any record; any metamodel change; C-12-style specialization decisions.

## 5. NOT-list

1. No records admitted.
2. No seed invented from metamodel artifacts (those are metamodel content, not enterprise information models — boundary muddying rejected at planning).
3. No relationship assertions (dea:structures targets await canonical DataEntity/InformationAsset ids — available, but no model exists to assert from).
