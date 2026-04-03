# NCREM Ontology v1.1 Release Notes

Release date: `2026-04-03`

## Summary

`v1.1` is the current recommended release of the NCREM ontology.

This release represents the first public update after `v1.0` and includes both validation fixes and broader ontology hardening work.

## Main Changes Since v1.0

- added ontology release metadata, including `owl:versionIRI`, `owl:imports`, and `dcterms:issued`
- normalized the KPI alignment to the ETSI SAREF4City namespace
- completed labels and descriptions for local NCREM classes and properties
- added domain and range declarations across local NCREM properties
- improved class modeling for concepts such as `Setpoint`, `Duration`, `Image`, and green-roof layers
- introduced supporting mobility and traffic classes such as `ParkingFacility`, `ParkingSpace`, `MobilityStation`, `RoadSegment`, and `TransitStop`
- replaced problematic local class-style reuse of external terms with local concepts such as `DataFormat` and `Solar_Reflectance`
- added lightweight disjointness axioms for cleaner reasoning

## Validation

Validation result for `NCREM_Ontology_v1.1.ttl`:

- RDF/Turtle parse: OK
- Triples: 1203
- Classes: 253
- Object properties: 47
- Datatype properties: 13
- Annotation properties: 15
- Findings: none

## Recommended File

- [`../NCREM_Ontology_v1.1.ttl`](../NCREM_Ontology_v1.1.ttl)
