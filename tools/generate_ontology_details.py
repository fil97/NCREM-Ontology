import sys
from pathlib import Path

from rdflib import BNode, Graph, RDF, RDFS, OWL, URIRef
from rdflib.namespace import DCTERMS, SKOS


NCREM_NAMESPACE = "http://www.semanticweb.org/filippos/ontologies/2023/4/NCREM_Ontology#"


def one_literal(graph, subject, predicates):
    for predicate in predicates:
        for value in graph.objects(subject, predicate):
            if not isinstance(value, BNode):
                return str(value).replace("\n", " ").strip()
    return ""


def clean_cell(value):
    return " ".join(value.replace("|", "\\|").split())


def term_rows(graph, rdf_type):
    rows = []
    for subject in sorted(set(graph.subjects(RDF.type, rdf_type)), key=str):
        if isinstance(subject, BNode):
            continue
        label = one_literal(graph, subject, [RDFS.label, SKOS.prefLabel])
        description = one_literal(
            graph,
            subject,
            [SKOS.definition, RDFS.comment, DCTERMS.description],
        )
        rows.append((str(subject), label, description))
    return rows


def write_table(lines, rows):
    lines.append("| URI | Label | Description |")
    lines.append("| --- | --- | --- |")
    for uri, label, description in rows:
        lines.append(
            f"| {clean_cell(uri)} | {clean_cell(label)} | {clean_cell(description)} |"
        )
    lines.append("")


def main():
    if len(sys.argv) != 3:
        raise SystemExit(
            "Usage: python generate_ontology_details.py INPUT.ttl OUTPUT.md"
        )

    source = Path(sys.argv[1])
    output = Path(sys.argv[2])

    graph = Graph()
    graph.parse(source, format="turtle")

    class_count = len(set(graph.subjects(RDF.type, OWL.Class)))
    object_property_count = len(set(graph.subjects(RDF.type, OWL.ObjectProperty)))
    datatype_property_count = len(set(graph.subjects(RDF.type, OWL.DatatypeProperty)))
    annotation_property_count = len(set(graph.subjects(RDF.type, OWL.AnnotationProperty)))

    ncrem_class_count = len(
        {term for term in graph.subjects(RDF.type, OWL.Class) if str(term).startswith(NCREM_NAMESPACE)}
    )
    ncrem_object_property_count = len(
        {
            term
            for term in graph.subjects(RDF.type, OWL.ObjectProperty)
            if str(term).startswith(NCREM_NAMESPACE)
        }
    )
    ncrem_datatype_property_count = len(
        {
            term
            for term in graph.subjects(RDF.type, OWL.DatatypeProperty)
            if str(term).startswith(NCREM_NAMESPACE)
        }
    )
    import_count = len(set(graph.objects(None, OWL.imports)))

    classes = term_rows(graph, OWL.Class)
    object_properties = term_rows(graph, OWL.ObjectProperty)
    datatype_properties = term_rows(graph, OWL.DatatypeProperty)
    annotation_properties = term_rows(graph, OWL.AnnotationProperty)

    lines = [
        "# NCREM Ontology Details",
        "",
        f"This document provides a generated overview of the terms defined or reused in `{source.name}`.",
        "",
        "## Summary",
        "",
        f"- Source file: `{source.name}`",
        f"- Triples: {len(graph)}",
        f"- Classes: {class_count}",
        f"- Object properties: {object_property_count}",
        f"- Datatype properties: {datatype_property_count}",
        f"- Annotation properties: {annotation_property_count}",
        f"- NCREM classes: {ncrem_class_count}",
        f"- NCREM object properties: {ncrem_object_property_count}",
        f"- NCREM datatype properties: {ncrem_datatype_property_count}",
        f"- `owl:imports` declarations: {import_count}",
        "",
        "## Classes",
        "",
    ]
    write_table(lines, classes)
    lines.extend(["## Object Properties", ""])
    write_table(lines, object_properties)
    lines.extend(["## Datatype Properties", ""])
    write_table(lines, datatype_properties)
    lines.extend(["## Annotation Properties", ""])
    write_table(lines, annotation_properties)

    output.write_text("\n".join(lines), encoding="utf-8")


if __name__ == "__main__":
    main()
