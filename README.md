# NCREM Ontology

Neighborhood Construction, Renovation & Energy Management (NCREM) Ontology

Current release: `v1.2.1`
Recommended ontology file: [`NCREM_Ontology_v1.2.1.ttl`](NCREM_Ontology_v1.2.1.ttl)

## Overview

The NCREM ontology provides a semantic model for neighborhoods, buildings, renovation workflows, energy systems, environmental monitoring, agent-based modelling, UHI scenario assessment, geospatial features, recommendations, and neighborhood-scale KPIs.

It is designed to support:

- semantic data integration for building and district data
- ontology-based digital twins
- KPI modeling for energy, comfort, LCA, UHI, mobility, exposure, and ABM use cases
- interoperability with well-known ontologies such as Brick, SAREF, BOT, GeoSPARQL, PROV-O, OWL-Time, DCAT, RDF Data Cube, SOSA/SSN, and QUDT

## What Is In This Repository

- [`NCREM_Ontology_v1.2.1.ttl`](NCREM_Ontology_v1.2.1.ttl): current ontology release
- [`NCREM_Ontology_v1.2.ttl`](NCREM_Ontology_v1.2.ttl): previous public release
- [`NCREM_Ontology_v1.1.ttl`](NCREM_Ontology_v1.1.ttl): earlier public release
- [`NCREM_Ontology_v1.0.ttl`](NCREM_Ontology_v1.0.ttl): original release
- [`docs/ontology_details.md`](docs/ontology_details.md): generated term documentation for `v1.2.1`
- [`docs/property_alignment_v1.2.1.md`](docs/property_alignment_v1.2.1.md): mapping decisions and semantic rationale for local properties
- [`docs/release_notes_v1.2.1.md`](docs/release_notes_v1.2.1.md): release summary for `v1.2.1`
- [`docs/release_notes_v1.2.md`](docs/release_notes_v1.2.md): release summary for `v1.2`
- [`docs/release_notes_v1.1.md`](docs/release_notes_v1.1.md): release summary for `v1.1`
- [`CITATION.cff`](CITATION.cff): citation metadata
- [`LICENSE`](LICENSE): CC BY 4.0 license

## Version 1.2.1 Highlights

- preserves `v1.2` and adds `NCREM_Ontology_v1.2.1.ttl` as the recommended ontology file
- selectively reuses classes and properties from Brick, SAREF, BOT, GeoSPARQL, PROV-O, OWL-Time, DCAT, RDF Data Cube, SOSA/SSN, QUDT, and supporting vocabularies under their original namespace IRIs
- does not use `owl:imports`; referenced vocabularies are documented with `dcterms:references`
- adds formal superproperty mappings for nine NCREM relationships where their semantics and domains are compatible with PROV-O, Schema.org, Brick, Dublin Core, or BIMERR
- clarifies the distinct semantics of local workflow-duration, configuration-parameter, and material-bank associations instead of asserting unsafe equivalence
- corrects the selective Brick hierarchy so that `brick:Sensor` specializes `brick:Point`, consistently with Brick 1.3
- keeps every NCREM v1.2 class and property IRI unchanged, so existing data and queries remain compatible
- documents mapping decisions and the reasons for retaining project-specific relationships
- parses cleanly as RDF/Turtle

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

## Namespaces

The `v1.2.1` release declares the following prefixes in the ontology file:

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
| `bot` | `https://w3id.org/bot#` |
| `dcat` | `http://www.w3.org/ns/dcat#` |
| `geo` | `http://www.opengis.net/ont/geosparql#` |
| `prov` | `http://www.w3.org/ns/prov#` |
| `qb` | `http://purl.org/linked-data/cube#` |
| `saref4ener` | `https://saref.etsi.org/saref4ener/` |
| `ssn` | `http://www.w3.org/ns/ssn/` |
| `sosa` | `http://www.w3.org/ns/sosa/` |
| `time` | `http://www.w3.org/2006/time#` |
| `foaf` | `http://xmlns.com/foaf/0.1/` |
| `org` | `http://www.w3.org/ns/org#` |
| `schema` | `https://schema.org/` |
| `seas` | `https://w3id.org/seas/` |
| `s4agri` | `https://saref.etsi.org/saref4agri/` |
| `s4bldg` | `https://saref.etsi.org/saref4bldg/` |
| `s4envi` | `https://saref.etsi.org/saref4envi/` |
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
- [`docs/property_alignment_v1.2.1.md`](docs/property_alignment_v1.2.1.md)
- [`docs/release_notes_v1.2.1.md`](docs/release_notes_v1.2.1.md)
- [`docs/release_notes_v1.2.md`](docs/release_notes_v1.2.md)

To regenerate the term documentation:

```bash
python -m pip install -r tools/requirements.txt
python tools/generate_ontology_details.py NCREM_Ontology_v1.2.1.ttl docs/ontology_details.md
python tools/validate_release.py NCREM_Ontology_v1.2.1.ttl
```

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
Filippos Lygerakis. NCREM Ontology v1.2.1. Technical University of Crete (TUC), 2026.
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
