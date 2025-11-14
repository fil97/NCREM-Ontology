
# 🏙️ NCREM Ontology

**Neighborhood Construction, Renovation & Energy Management (NCREM) Ontology**  
📅 Version: 1.0  
👤 Created by: *Filippos Lygerakis*, Environmental Engineer, PhD, MSc, Technical University of Crete (TUC)

---

## 📘 Description

The **NCREM ontology** provides a semantic framework for representing **neighborhoods**, **buildings**, and their associated **construction**, **renovation**, and **energy management** processes. It supports interoperability across systems and integrates existing ontologies such as:

- [Brick Schema](https://brickschema.org)
- [SAREF](https://saref.etsi.org)
- [SAREF4City](https://saref.etsi.org/saref4city)
- [QUDT](http://www.qudt.org)

It is designed to support **Key Performance Indicators (KPIs)**, energy systems, digital twins, and lifecycle analyses of smart cities and sustainable construction.

---

## 📛 Namespaces

| Prefix      | Namespace URI |
|-------------|----------------|
| `xml`       | `http://www.w3.org/XML/1998/namespace` |
| `kpi`       | `http://bimerr.iot.linkeddata.es/def/key-performance-indicator#` |
| `mat`       | `http://bimerr.iot.linkeddata.es/def/material-properties#` |
| `ssn`       | `http://www.w3.org/ns/ssn/` |
| `core`      | `https://saref.etsi.org/core/` |
| `qudt`      | `http://qudt.org/schema/qudt/` |
| `seas`      | `https://w3id.org/seas/` |
| `skos`      | `http://www.w3.org/2004/02/skos/core#` |
| `weat`      | `https://bimerr.iot.linkeddata.es/def/weather` |
| `brick`     | `https://brickschema.org/schema/Brick#` |
| `ncrem`     | `http://www.semanticweb.org/filippos/ontologies/2023/4/NCREM_Ontology#` |
| `shacl`     | `http://www.w3.org/ns/shacl#` |
| `s4agri`    | `https://saref.etsi.org/saref4agri/` |
| `s4bldg`    | `https://saref.etsi.org/saref4bldg/` |
| `s4city`    | `https://saref.etsi.org/saref4city/` |
| `s4ener`    | `https://saref.etsi.org/saref4ener/` |
| `dcterms`   | `http://purl.org/dc/terms/` |
| `building`  | `https://bimerr.iot.linkeddata.es/def/building#` |

---

## 🧠 Ontology Metrics

- **🧩 Classes**: 239  
- **🔗 Object Properties**: 48  
- **📊 Data Properties**: 13  

---

## 📚 Full Ontology Documentation

For a complete list of all classes and properties with URIs and definitions, see  
👉 [`docs/ontology_details.md`](docs/ontology_details.md)

---

## 📎 Example SPARQL Query

```sparql
PREFIX ncrem: <http://www.semanticweb.org/filippos/ontologies/2023/4/NCREM_Ontology#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>

SELECT ?class ?label WHERE {
  ?class a owl:Class .
  OPTIONAL { ?class rdfs:label ?label }
}
LIMIT 10
```

---

## 📄 License

This ontology is licensed under the **Creative Commons Attribution 4.0 International (CC BY 4.0)**.


Creative Commons Attribution 4.0 International (CC BY 4.0)

You are free to:

- **Share** — copy and redistribute the material in any medium or format
- **Adapt** — remix, transform, and build upon the material for any purpose, even commercially.

Under the following terms:

- **Attribution** — You must give appropriate credit, provide a link to the license, and indicate if changes were made. 
  You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

No additional restrictions — You may not apply legal terms or technological measures that legally restrict others from doing anything the license permits.

License link: [https://creativecommons.org/licenses/by/4.0/](https://creativecommons.org/licenses/by/4.0/)


---

## 📚 Citation

If you use this ontology in your research or project, please cite:

```
Filippos Lygerakis, Environmental Engineer, MSc, Technical University of Crete (TUC). NCREM Ontology v1.0.
```


## 👥 Contributors

- Filippos Lygerakis – Author (Technical University of Crete)
- Nikolaos Kampelis - Contributor (Technical University of Crete)
- Dionysia Kolokotsa - Contributor (Technical University of Crete)


---

## 📢 Funding Acknowledgment

This ontology was developed within the scope of the [PROBONO](https://www.probonoh2020.eu/) project, funded by the European Union’s Horizon 2020 research and innovation programme under grant agreement No. **101037075**.

The PROBONO project aims to deliver scalable and sustainable energy-positive and zero-carbon urban solutions, contributing to the European Green Deal objectives and the transformation of the built environment.
