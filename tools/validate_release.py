import sys
from pathlib import Path

from rdflib import Graph, RDF, RDFS, OWL
from rdflib.namespace import DCTERMS, SKOS


NCREM_NAMESPACE = "http://www.semanticweb.org/filippos/ontologies/2023/4/NCREM_Ontology#"
LEGACY_BRICK_NAMESPACE = "https://brickschema.org/schema/1.3/Brick#"


def local(term):
    return str(term).startswith(NCREM_NAMESPACE)


def main():
    if len(sys.argv) != 2:
        raise SystemExit("Usage: python validate_release.py INPUT.ttl")

    source = Path(sys.argv[1])
    graph = Graph()
    graph.parse(source, format="turtle")

    classes = set(graph.subjects(RDF.type, OWL.Class))
    object_properties = set(graph.subjects(RDF.type, OWL.ObjectProperty))
    datatype_properties = set(graph.subjects(RDF.type, OWL.DatatypeProperty))
    annotation_properties = set(graph.subjects(RDF.type, OWL.AnnotationProperty))
    local_terms = {
        *filter(local, classes),
        *filter(local, object_properties),
        *filter(local, datatype_properties),
    }

    missing_labels = sorted(
        str(term) for term in local_terms if not any(graph.objects(term, RDFS.label))
    )
    missing_descriptions = sorted(
        str(term)
        for term in local_terms
        if not any(graph.objects(term, SKOS.definition))
        and not any(graph.objects(term, RDFS.comment))
        and not any(graph.objects(term, DCTERMS.description))
    )
    imports = set(graph.objects(None, OWL.imports))
    legacy_brick_terms = sorted(
        {
            str(term)
            for subject, predicate, obj in graph
            if predicate != DCTERMS.references
            for term in (subject, predicate, obj)
            if str(term).startswith(LEGACY_BRICK_NAMESPACE)
        }
    )
    local_property_alignments = {
        term
        for term in object_properties | datatype_properties
        if local(term) and any(graph.objects(term, RDFS.subPropertyOf))
    }

    ontology_nodes = set(graph.subjects(RDF.type, OWL.Ontology))
    errors = []
    if len(ontology_nodes) != 1:
        errors.append(f"expected one owl:Ontology node, found {len(ontology_nodes)}")
    for ontology in ontology_nodes:
        if not any(graph.objects(ontology, OWL.versionIRI)):
            errors.append("ontology is missing owl:versionIRI")
        if not any(graph.objects(ontology, OWL.versionInfo)):
            errors.append("ontology is missing owl:versionInfo")
        if not any(graph.objects(ontology, DCTERMS.issued)):
            errors.append("ontology is missing dcterms:issued")
    if imports:
        errors.append(f"selective release contains {len(imports)} owl:imports declaration(s)")
    if missing_labels:
        errors.append(f"{len(missing_labels)} local terms lack rdfs:label")
    if missing_descriptions:
        errors.append(f"{len(missing_descriptions)} local terms lack a definition or comment")
    if legacy_brick_terms:
        errors.append(f"{len(legacy_brick_terms)} terms use the legacy versioned Brick namespace")

    print(f"Source: {source.name}")
    print("RDF/Turtle parse: OK")
    print(f"Triples: {len(graph)}")
    print(f"Classes: {len(classes)}")
    print(f"Object properties: {len(object_properties)}")
    print(f"Datatype properties: {len(datatype_properties)}")
    print(f"Annotation properties: {len(annotation_properties)}")
    print(f"NCREM classes: {sum(map(local, classes))}")
    print(f"NCREM object properties: {sum(map(local, object_properties))}")
    print(f"NCREM datatype properties: {sum(map(local, datatype_properties))}")
    print(f"NCREM properties with a formal external superproperty: {len(local_property_alignments)}")
    print(f"owl:imports declarations: {len(imports)}")
    print(f"Local terms without a label: {len(missing_labels)}")
    print(f"Local terms without a definition or comment: {len(missing_descriptions)}")
    print(f"Legacy versioned Brick terms: {len(legacy_brick_terms)}")

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1)

    print("Release validation: PASS")


if __name__ == "__main__":
    main()
