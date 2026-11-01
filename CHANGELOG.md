# Changelog

All notable changes to this catalog are documented here. Format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### `CR-IM-CAT-04` — pilot tranche (Customer, Invoice, Order)

First three canonical InformationModel records under the CR-IM-CAT-03 contract: conceptual-form models for the Customer, Invoice, and Order business objects, each with a full attribute dictionary, constraints, a represents assertion onto the canonical BO id, and two-part evidence (BO record + TMF published authority + committed artifact). dea:structures assertions deferred until downstream stand-ups. CATALOG.yaml: 3 canonical.


### `CR-IM-CAT-03` — evidence-input contract

Three evidence-input channels established as normative (author-in-repo primary via business-object attribute models; external anchoring via TMF SID/Open APIs where the domain has one; opportunistic harvest sweep). Model-artifact contract: canonical artifacts committed at models/<slug>.yaml, two-way bound to their records (Gate 7 enforces shape, BO-id form, and the citation binding). Zero records admitted.


### Added

- Catalog bootstrapped from `dea-metaframework/tools/catalog-repo-template/`
  (TEMPLATE_VERSION 0.1.0). Authored under CR-CATALOG-STRUCT-06b.
