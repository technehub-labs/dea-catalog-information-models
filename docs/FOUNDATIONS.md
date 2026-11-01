# Foundations: Information Model Catalog

This document records the method the catalogue follows: cardinal scope,
exclusions, admission criteria, allocation, cross-catalogue policy, and the
decision register. The record documentation standard
([RECORD-STANDARD.md](RECORD-STANDARD.md)) and the schema projection carry
the operational contract.

## 1. Cardinal scope

**Information Model** — A formal model that specifies the structure, semantics, and constraints of information for a domain - the conceptual or logical blueprint from which Data Entities are shaped and Information Assets take form. Distinct from Information Class (the sensitivity/regulatory band) and Information Asset (the consumable form).

## 2. What is deliberately excluded

Boundaries against sibling entity types are governed by the metamodel
definitions; anything that is not a information model record
belongs to its owning catalogue (see the metamodel's `catalog_repo`
allocations).

## 3. Admission criteria and evidence ladder

1. The record describes a information model per the metamodel definition.
2. At least one evidence source verifiably exists at admission time
   (`repository-path`, `system-of-record`, or `published-document`).
3. Relationship instances are asserted only against canonical target ids
   that exist; absence is honest (no local substitutes).

Evidence ladder (asserted in `provenance.ladder_passage`):
candidate → corroborated → reviewed → canonical.

## 4. Allocation

`dea:entity-information-model` (alias `IM`), layer L4 / L4-information-knowledge, pinned against
OpenDEAM v0.9.0. Validated remotely by `validate-allocation.yml`
and locally by Gate 2. Upstream pins live in `dependencies.yaml`.

## 5. Cross-catalogue reference policy

1. Crosswalks and references are recorded on the asserting record's side,
   as typed relationship instances (metamodel relationship-instance
   contract).
2. Assertions wait for canonical targets: no scheme invention where a
   sibling id scheme does not exist.
3. Gates never resolve remote repositories; vendored registry snapshots
   carry the offline contract where a specific target family is asserted.

## 6. Decision-points register

| # | Decision | Status |
|---|---|---|
| D-1 | Methodology-first bring-up: no records before the kit and population CR | Adopted (CR-IM-CAT-01) |
| D-2 | Hybrid pointer: identity keys for the regenerator + `metamodel:` allocation block for the root-model validator | Adopted (CR-IM-CAT-01) |
| D-3 | Record ids take the `dea:information-model-<slug>` form (information-classes `dea:`-prefix precedent) | Adopted (CR-IM-CAT-01) |
| D-4 | Admission ladder: candidate → corroborated → reviewed → canonical | Adopted (CR-IM-CAT-01) |
| D-5 | Evidence-only admission: no record without a verifiable source; population plans document the wait | Adopted (CR-IM-CAT-01) |
| D-6 | `CATALOG.yaml` is committed, not ignored (template deviation): the freshness gate diffs the committed index | Adopted (CR-IM-CAT-01) |

## 7. Population plan

Initial population is evidence-gated. Candidate seed sources are named in
the population CR; where none are verifiable today, the catalogue stays at
zero canonical records with this section recording why and what would
unlock population.

**Landed (CR-IM-CAT-02):** candidate sources — the domain-ontology pillar
(`dea-catalog-ontologies`, first ontology = canonical candidate, model_form
ontology), business-object attribute models (U-1 follow-on), ESA/EO
artifacts, and integration-interface payload schemas. Admission requires a
cited producing artifact, a declared `model_form`, and the boundary test
(specifies structure via `dea:structures`; not a class, a consumable form,
or a persistent structure).

## 8. Evidence-input channels (CR-IM-CAT-03)

Unlike every sibling catalog, information models did not exist as formal artifacts at stand-up — evidence must be **established**, not just harvested. Three channels, in priority order:

1. **Author-in-repo (primary).** Business-object attribute models for the canonical Business Objects: authored at `models/<slug>.yaml`, citing the canonical BO record as provenance and asserting `represents` onto it. The authoring CR is the ladder's start.
2. **Chain corroboration (internal).** Attribute sets are corroborated against the canonical Business Object definition and the sibling models along the Agreement → Offering → Product → Service → Resource → Entity chain (each model records its chain position; chain neighbours are reviewed together). External published authorities may be cited as descriptive references, never as the corroboration basis.
3. **Harvest sweep (opportunistic).** Model-shaped artifacts appearing in org repos (payload schemas, DDL, ontologies) are census candidates for `model_form: schema|ontology` records and the first `dea:structures` assertions.

The `dea:structures` edge lights up when a downstream DataEntity or InformationAsset is stood up shaped by a model record. The model-artifact contract is normative in RECORD-STANDARD.md section 4 (two-part evidence: provenance source + committed artifact; Gate 7 enforces).
