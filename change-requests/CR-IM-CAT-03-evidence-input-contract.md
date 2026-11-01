# CR-IM-CAT-03: Evidence-Input Contract

| Field | Value |
|---|---|
| **CR** | CR-IM-CAT-03 |
| **Title** | Evidence-input contract: three channels, model-artifact contract, Gate 7 |
| **Status** | Landed |
| **Layer** | Catalogue (L4 Information & Knowledge) |
| **Programme** | Information Model governance chain |
| **Repository** | `technehub-labs/dea-catalog-information-models` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-11-01 |
| **Depends on** | CR-IM-CAT-01, CR-IM-CAT-02 |
| **Trigger** | Owner directive: establish the approach for evidence inputs. Unlike every sibling catalog, information models do not exist as formal artifacts at stand-up — the evidence pipeline must be author-first, with each production act generating its own evidence. |

## 1. Executive summary

Establishes the evidence-input approach as normative: **three channels** (author-in-repo primary, external anchoring for corroboration, opportunistic harvest), the **model-artifact contract** (canonical artifact committed at `models/<slug>.yaml`, two-way bound to its record), and **Gate 7** which enforces the contract mechanically. Zero records admitted.

## 2. The three channels

1. **Author-in-repo (primary).** Business-object attribute models for the 74 canonical Business Objects: authored at `models/<slug>.yaml`, citing the canonical BO record as provenance, asserting `represents` onto it. The authoring CR starts the ladder.
2. **External anchoring (corroboration).** Attribute sets cross-checked against a published external authority where the domain has one (TM Forum SID / Open APIs for the telecom-flavored domains). Where none covers, corroboration is marked internal-only.
3. **Harvest sweep (opportunistic).** Model-shaped artifacts in org repos (payload schemas, DDL, ontologies) are census candidates for `model_form: schema|ontology` records and the first `dea:structures` assertions.

## 3. The two-part evidence rule

A canonical InformationModel record's evidence is two-part: (1) the **provenance source** where the semantics came from, and (2) the **committed artifact itself** — `models/<slug>.yaml`, repository-path evidence, diff-able and gate-checked. A record without its artifact is an assertion; an artifact without its record is ungoverned content. The pair is the admission unit.

## 4. Scope

In scope: RECORD-STANDARD section 4 (model artifact contract), FOUNDATIONS section 8 (channels) + D-10/D-11, `scripts/check_model_artifact.py` (Gate 7), workflow Step 7, this CR + registers + CHANGELOG.

Out of scope: any record or artifact admission (CR-IM-CAT-04); metamodel changes; diagrams-as-artifact (external references only).

## 5. Acceptance criteria

1. Gate 7 passes with 0 artifacts (vacuous), and the workflow carries Step 7.
2. FOUNDATIONS + RECORD-STANDARD carry the contract normatively.
3. All other gates unchanged and green.

## 6. NOT-list

1. No records or model artifacts admitted.
2. No metamodel changes; no widening of `specifies`.
3. No diagrams as canonical artifacts.
