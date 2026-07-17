# NCREM Ontology v1.2.1 Release Notes

Release date: `2026-07-17`

## Summary

`v1.2.1` is a non-breaking semantic-quality update to `v1.2`. It preserves all existing NCREM class and property IRIs while strengthening reuse transparency, property alignment, provenance semantics, and release documentation.

The release continues to use a selective ontology network without `owl:imports`. Referenced vocabularies are recorded using `dcterms:references`, and canonical external terms retain their source IRIs.

## Main Changes Since v1.2

- added nine defensible `rdfs:subPropertyOf` mappings for NCREM relationships:
  - `ncrem:hasAgent` to `prov:wasAttributedTo`
  - `ncrem:hasDependency` to `prov:wasInformedBy`
  - `ncrem:hasImage` to `schema:image`
  - `ncrem:hasLayer` to `mat:hasMaterialLayer`
  - `ncrem:hasSensor` to `brick:hasPoint`
  - `ncrem:hasTask` to `dcterms:hasPart`
  - `ncrem:assessesScenario` to `prov:used`
  - `ncrem:evaluatesMeasure` to `prov:used`
  - `ncrem:recommendsAction` to `schema:potentialAction`
- aligned `foaf:Agent` with `prov:Agent` and made the inherited PROV-O semantics of `prov:Plan` explicit in the selective network
- aligned `ncrem:RecommendedAction` with both `prov:Plan` and `schema:Action`
- corrected the selective Brick hierarchy from `brick:Sensor rdfs:subClassOf brick:Equipment` to the Brick 1.3 relationship `brick:Sensor rdfs:subClassOf brick:Point`
- clarified that `ncrem:hasDuration` expresses the planned duration of a workflow plan, rather than duplicating `time:hasDuration`, whose subject is a temporal entity
- clarified that `ncrem:hasParameter` links models, scenarios, workflows, or control configurations to input parameters, rather than duplicating SAREF `hasProperty`
- removed the ambiguous “uses or produces” wording from `ncrem:hasMaterialBank`; provenance-specific usage or generation should be asserted with `prov:used` or `prov:generated`
- expanded `dcterms:references` to document supporting vocabularies used by the selective ontology network
- added a property-alignment decision record and a reproducible release-validation script

## Compatibility

This patch is intended to be backward compatible:

- no NCREM class or property IRI was removed or renamed
- no local property was declared equivalent to an external property
- existing instance data and SPARQL queries using v1.2 NCREM IRIs remain valid
- the added superproperty axioms may produce additional, standards-aligned inferred triples when RDFS/OWL reasoning is enabled

## Technical Verification

Verification result for `NCREM_Ontology_v1.2.1.ttl`:

- RDF/Turtle parse: OK
- Triples: 1362
- Classes: 285
- Object properties: 60
- Datatype properties: 16
- Annotation properties: 13
- NCREM classes: 172
- NCREM object properties: 21
- NCREM datatype properties: 8
- NCREM properties with a formal external superproperty: 9
- `owl:imports` declarations: 0
- local NCREM classes and properties without a label: 0
- local NCREM classes and properties without a definition or comment: 0

These checks establish syntax, release consistency, documentation coverage, and selected namespace conformance. They are not presented as a complete logical-validation or ontology-quality benchmark.

## Recommended File

- [`../NCREM_Ontology_v1.2.1.ttl`](../NCREM_Ontology_v1.2.1.ttl)
