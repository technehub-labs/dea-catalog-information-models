# Change Requests: dea-catalog-information-models

This index tracks every change request that lands on this repository.

| CR | Title | Status | Notes |
|----|-------|--------|-------|
| [CR-IM-CAT-01](CR-IM-CAT-01-catalogue-foundation.md) | Catalogue foundation (kit bring-up) | Landed (this PR) | Standard kit: pointer, dependencies, schema projection, gates 1-6, workflows, FOUNDATIONS, record standard. No records admitted. |
| [CR-IM-CAT-02](CR-IM-CAT-02-population-plan.md) | Population plan (zero records) | Landed (this PR) | Candidate sources named: domain-ontology pillar, business-object attribute models, ESA/EO artifacts, interface payload schemas. Admission requires a producing artifact + model_form + the boundary test. Zero records. |
| [CR-IM-CAT-03](CR-IM-CAT-03-evidence-input-contract.md) | Evidence-input contract | Landed (this PR) | Three channels (author-in-repo primary, external anchoring, harvest sweep); model-artifact contract (models/<slug>.yaml two-way bound to its record; two-part evidence rule); Gate 7 wired. Zero records. |
| [CR-IM-CAT-04](CR-IM-CAT-04-pilot-tranche.md) | Pilot tranche (Customer, Invoice, Order) | Landed (this PR) | First three canonical records under the CR-IM-CAT-03 contract: conceptual models, represents onto canonical BO ids, TMF-anchored, two-part evidence. dea:structures deferred by design. |
| [CR-IM-CAT-05](CR-IM-CAT-05-scope-amendment.md) | Scope amendment (full BO coverage, chain lens, TMF withdrawn) | Landed (this PR) | D-12: all 74 BOs by ECF domain (7 tranches); D-13: internal-first corroboration, TMF anchoring withdrawn; pilot records re-based with chain positions. Zero new records. |
| CR-IM-CAT-02 | Initial population | Planned | Evidence-gated seed population per FOUNDATIONS §7. |

## Numbering

Series tag `CR-IM-CAT-NN`, sequential. Cross-repo CRs that touch this
repository are recorded here with their home-repo identifier.
