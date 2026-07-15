# NCREM Ontology v1.2 Release Notes

Release date: `2026-07-15`

## Summary

`v1.2` extends the NCREM ontology to support neighborhood-scale knowledge graphs, operational energy monitoring, UHI, KPI, mobility, recommendation, provenance, and ABM workflows developed in PROBONO.

The update preserves `v1.1` as the previous public release and adds `NCREM_Ontology_v1.2.ttl` as the recommended ontology file. The release follows a reuse-first policy: canonical external terms retain their source IRIs, while concepts or relationships absent from the selected vocabularies are created in the `ncrem:` namespace.

## Main Changes Since v1.1

- added selective reuse and documented references for BOT, GeoSPARQL, PROV-O, OWL-Time, DCAT, RDF Data Cube, SOSA/SSN, SAREF extensions, Brick 1.3, QUDT, and supporting vocabularies
- removed `owl:imports` declarations so that the release remains a self-contained selective ontology network; source vocabularies are recorded with `dcterms:references`
- retained generic concepts as external ontology terms instead of duplicating them as local NCREM classes
- added focused NCREM classes for project-specific concepts: `ABMModel`, `ABMScenario`, `UHIAssessmentModel`, `UHIMitigationMeasure`, `UHIHotspot`, `UHIReferenceZone`, `MaterialBank`, `MobilityScenario`, `MobilityIntervention`, `RecommendedAction`, `OccupantAction`, and `ScenarioAssessment`
- aligned existing local terms with external ontology concepts, including BOT building topology, GeoSPARQL features, PROV activities/entities/plans, OWL-Time temporal entities, SOSA sensors, and Schema.org image objects
- aligned `ncrem:Workflow` with `prov:Plan` and `ncrem:Task` with `prov:Activity`, connected by `ncrem:hasTask`
- aligned external time-series references with Brick 1.3 `brickref:TimeseriesReference`, `brickref:hasExternalReference`, `brickref:hasTimeseriesId`, and `brickref:storedAt`
- corrected accumulated charged and discharged energy classes to specialize SAREF `Energy`, rather than `Power`
- moved five concepts absent from Brick 1.3 into the NCREM namespace: `ncrem:Absolute_Humidity_Sensor`, `ncrem:Primary_Energy_Consumption`, `ncrem:Solar_Irradiance_Sensor`, `ncrem:Storage_System_Installed_Capacity`, and `ncrem:hasParameter`
- avoided adding restrictive local domain or range axioms to reused properties where the source vocabulary is intentionally more general
- added project-specific object properties for scenario assessment, evaluated measures, material banks, recommended actions, setpoint changes, workflow tasks, and local parameters
- removed the broader generic NCREM wrappers from the first v1.2 draft, including local model-run, dataset, KPI-observation, service, risk, image, and geospatial-layer wrappers, in favour of direct reuse of PROV-O, DCAT, RDF Data Cube, SOSA, GeoSPARQL, and Schema.org terms

## Technical Verification

Verification result for `NCREM_Ontology_v1.2.ttl`:

- RDF/Turtle parse: OK
- Triples: 1335
- Classes: 282
- Object properties: 58
- Datatype properties: 16
- Annotation properties: 13
- NCREM classes: 172
- NCREM object properties: 21
- NCREM datatype properties: 8
- `owl:imports` declarations: 0
- local NCREM classes and properties without a label: 0
- local NCREM classes and properties without a definition or comment: 0

These checks establish syntax, release consistency, term documentation, and selected namespace conformance. They are not presented as a complete logical-validation or ontology-quality benchmark.

## Compatibility Notes

The following IRIs appeared in an unpublished v1.2 draft but are not Brick 1.3 terms. Use the NCREM replacements in this release:

| Unpublished draft IRI | v1.2 release IRI |
| --- | --- |
| `brick:Absolute_Humidity_Sensor` | `ncrem:Absolute_Humidity_Sensor` |
| `brick:Primary_Energy_Consumption` | `ncrem:Primary_Energy_Consumption` |
| `brick:Solar_Irradiance_Sensor` | `ncrem:Solar_Irradiance_Sensor` |
| `brick:Storage_System_Installed_Capacity` | `ncrem:Storage_System_Installed_Capacity` |
| `brick:hasParameter` | `ncrem:hasParameter` |

## Recommended File

- [`../NCREM_Ontology_v1.2.ttl`](../NCREM_Ontology_v1.2.ttl)
