# CR-IM-CAT-05: Scope Amendment — Full Business-Object Coverage, Chain Lens, TMF Withdrawal

| Field | Value |
|---|---|
| **CR** | CR-IM-CAT-05 |
| **Title** | Scope amendment: all 74 Business Objects by ECF domain; the Agreement→Offering→Product→Service→Resource→Entity chain as modeling lens; TMF anchoring withdrawn |
| **Status** | Landed |
| **Layer** | Catalogue (L4 Information & Knowledge) |
| **Programme** | Information Model governance chain |
| **Repository** | `technehub-labs/dea-catalog-information-models` |
| **Author** | Emmanuel A. Otchere |
| **Date** | 2026-11-01 |
| **Depends on** | CR-IM-CAT-03, CR-IM-CAT-04 |
| **Trigger** | Owner directive: drop TMF anchoring; cover ALL business objects in the initial scope, organized by ECF domain, considering the Agreement→Offering→Product→Service→Resource→Entity chain. |

## 1. Decisions (owner-ratified)

- **D-12 (scope):** the initial scope is ALL 74 canonical Business Objects, tranched by ECF domain (party-relationship 14, enablement-operations 22, finance-accounting 15, product-value 9, governance-existence 7, strategy-direction 4, agency-organization 3; the three pilot records count toward their domains).
- **D-13 (corroboration):** internal-first — the canonical BO definition plus the sibling models along the chain. TMF anchoring is withdrawn; published standards may be cited as descriptive references only. The three pilot records are re-based accordingly.
- **The chain lens:** every model artifact records its `chain_position` (agreement | offering | service | product | resource | entity | party | enablement | work | location), derived from the BO's object_class; models along the chain are reviewed together and reference their neighbours.

## 2. Chain mapping (object_class → chain position)

legal-instrument → agreement; offering → offering; resource → resource; transaction + financial-instrument → entity; party → party; technology-control → enablement; work-item → work; location → location.

## 3. Tranche plan (7 domain CRs)

| Tranche | ECF domain | Models (new) |
|---|---|---|
| T-party | party-relationship | 13 (Customer done) |
| T-enablement | enablement-operations | 21 (Order done) |
| T-finance | finance-accounting | 14 (Invoice done) |
| T-product | product-value | 9 |
| T-governance | governance-existence | 7 |
| T-strategy | strategy-direction | 4 |
| T-agency | agency-organization | 3 |

## 4. Changes in this CR

1. The three pilot records + artifacts + READMEs re-based (TMF published-document sources removed; chain position recorded; corroboration rationale rewritten internal-first).
2. FOUNDATIONS channel 2 rewritten; D-12/D-13 adopted. RECORD-STANDARD corroboration wording re-based.
3. Zero new records in this CR (tranches follow).

## 5. NOT-list

1. No new models in this CR.
2. No metamodel changes.
3. TMF references may survive as descriptive prose only; never as evidence sources.
