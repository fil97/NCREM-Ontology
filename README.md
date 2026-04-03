# NCREM Ontology

Neighborhood Construction, Renovation & Energy Management (NCREM) Ontology

Current release: `v1.1`
Recommended ontology file: [`NCREM_Ontology_v1.1.ttl`](NCREM_Ontology_v1.1.ttl)

## Overview

The NCREM ontology provides a semantic model for neighborhoods, buildings, renovation workflows, energy systems, environmental monitoring, comfort indicators, and neighborhood-scale KPIs.

It is designed to support:

- semantic data integration for building and district data
- ontology-based digital twins
- KPI modeling for energy, comfort, LCA, and UHI use cases
- interoperability with well-known ontologies such as Brick and SAREF

## What Is In This Repository

- [`NCREM_Ontology_v1.1.ttl`](NCREM_Ontology_v1.1.ttl): latest validated ontology release
- [`NCREM_Ontology_v1.0.ttl`](NCREM_Ontology_v1.0.ttl): original release
- [`docs/ontology_details.md`](docs/ontology_details.md): generated term documentation for `v1.1`
- [`docs/release_notes_v1.1.md`](docs/release_notes_v1.1.md): release summary for `v1.1`
- [`CITATION.cff`](CITATION.cff): citation metadata
- [`LICENSE`](LICENSE): CC BY 4.0 license

## Version 1.1 Highlights

- adds ontology release metadata such as `owl:versionIRI`, `owl:imports`, and `dcterms:issued`
- normalizes the KPI alignment with the ETSI SAREF4City namespace
- strengthens local semantics with labels, definitions, domains, and ranges across local NCREM terms
- improves concept modeling for setpoints, duration, images, green-roof layers, and material layers
- introduces supporting mobility and traffic classes used by existing properties
- adds lightweight disjointness axioms for cleaner reasoning
- validates cleanly with no ontology findings in the current validation workflow

## Validation Summary

Validation result for `NCREM_Ontology_v1.1.ttl`:

- RDF/Turtle parse: OK
- Triples: 1203
- Classes: 253
- Object properties: 47
- Datatype properties: 13
- Annotation properties: 15

## Namespaces

The `v1.1` release declares the following prefixes in the ontology file:

| Prefix | Namespace URI |
| --- | --- |
| `owl` | `http://www.w3.org/2002/07/owl#` |
| `rdf` | `http://www.w3.org/1999/02/22-rdf-syntax-ns#` |
| `xml` | `http://www.w3.org/XML/1998/namespace` |
| `xsd` | `http://www.w3.org/2001/XMLSchema#` |
| `core` | `https://saref.etsi.org/core/` |
| `qudt` | `http://qudt.org/schema/qudt/` |
| `rdfs` | `http://www.w3.org/2000/01/rdf-schema#` |
| `skos` | `http://www.w3.org/2004/02/skos/core#` |
| `brick` | `https://brickschema.org/schema/Brick#` |
| `ncrem` | `http://www.semanticweb.org/filippos/ontologies/2023/4/NCREM_Ontology#` |
| `shacl` | `http://www.w3.org/ns/shacl#` |
| `s4city` | `https://saref.etsi.org/saref4city/` |
| `dcterms` | `http://purl.org/dc/terms/` |
| `saref4ener` | `https://saref.etsi.org/saref4ener/` |
| `ssn` | `http://www.w3.org/ns/ssn/` |
| `sosa` | `http://www.w3.org/ns/sosa/` |
| `foaf` | `http://xmlns.com/foaf/0.1/` |
| `org` | `http://www.w3.org/ns/org#` |
| `schema` | `https://schema.org/` |
| `seas` | `https://w3id.org/seas/` |
| `s4agri` | `https://saref.etsi.org/saref4agri/` |
| `s4bldg` | `https://saref.etsi.org/saref4bldg/` |
| `building` | `http://bimerr.iot.linkeddata.es/def/building#` |
| `mat` | `http://bimerr.iot.linkeddata.es/def/material-properties#` |
| `weat` | `https://bimerr.iot.linkeddata.es/def/weather#` |
| `gtfs` | `http://vocab.gtfs.org/terms#` |
| `brickref` | `https://brickschema.org/schema/Brick/ref#` |
| `saref` | `https://w3id.org/saref#` |
| `kpi` | `http://bimerr.iot.linkeddata.es/def/key-performance-indicator#` |

## Documentation

For a complete list of classes and properties with their URIs, labels, and descriptions, see:

- [`docs/ontology_details.md`](docs/ontology_details.md)
- [`docs/release_notes_v1.1.md`](docs/release_notes_v1.1.md)

## Example SPARQL Query

```sparql
PREFIX ncrem: <http://www.semanticweb.org/filippos/ontologies/2023/4/NCREM_Ontology#>
PREFIX owl: <http://www.w3.org/2002/07/owl#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?class ?label WHERE {
  ?class a owl:Class .
  FILTER(STRSTARTS(STR(?class), STR(ncrem:)))
  OPTIONAL { ?class rdfs:label ?label }
}
ORDER BY ?class
LIMIT 20
```

## Citation

If you use this ontology, please cite it as:

```text
Filippos Lygerakis. NCREM Ontology v1.1. Technical University of Crete (TUC), 2026.
```

Machine-readable citation metadata is provided in [`CITATION.cff`](CITATION.cff).

## Contributors

- Filippos Lygerakis, Technical University of Crete (TUC)
- Nikolaos Kampelis, Cyprus Institute
- Dionysia Kolokotsa, Technical University of Crete (TUC)

## License

This ontology is distributed under the Creative Commons Attribution 4.0 International License (CC BY 4.0).

License URL:

- <https://creativecommons.org/licenses/by/4.0/>

## Funding

This ontology was developed within the scope of the PROBONO project, funded by the European Union's Horizon 2020 research and innovation programme under grant agreement No. `101037075`.
