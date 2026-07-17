# NCREM v1.2.1 Property-Alignment Decisions

This record explains the reuse decisions made in the `v1.2.1` maintenance release. A lexical similarity was not treated as sufficient evidence for equivalence. Mappings were added only where the local relation is a defensible semantic specialization of an external relation and its domain/range use is compatible.

## Formal Superproperty Mappings

| NCREM property | External superproperty | Rationale |
| --- | --- | --- |
| `ncrem:hasAgent` | `prov:wasAttributedTo` | A workflow is aligned with `prov:Plan`, hence with a PROV entity. The local relation assigns responsibility for authoring, owning, or maintaining that plan. Executed activities should use `prov:wasAssociatedWith` directly. |
| `ncrem:hasDependency` | `prov:wasInformedBy` | NCREM tasks are PROV activities; a task dependency is a specialized activity-to-activity dependency. |
| `ncrem:hasImage` | `schema:image` | The local object is an `ncrem:Image`, aligned with `schema:ImageObject`; the local relation narrows the general Schema.org image relation. |
| `ncrem:hasLayer` | `mat:hasMaterialLayer` | Both relations connect a construction/material assembly to a material layer. |
| `ncrem:hasSensor` | `brick:hasPoint` | The local range is a Brick sensor, and the relation states that the subject has that sensor point. |
| `ncrem:hasTask` | `dcterms:hasPart` | A task is represented as a constituent activity of a workflow plan. |
| `ncrem:assessesScenario` | `prov:used` | A scenario assessment is a PROV activity that uses the scenario entity it evaluates. |
| `ncrem:evaluatesMeasure` | `prov:used` | A scenario assessment is a PROV activity that uses the plan or measure under evaluation. |
| `ncrem:recommendsAction` | `schema:potentialAction` | A recommendation artifact points to a potential action; the local property gives that relation recommendation-specific meaning. |

## Local Relations Retained Without a Formal Mapping

| NCREM property | Decision |
| --- | --- |
| `ncrem:hasDuration` | Retained for the planned duration of a workflow plan. It is not mapped to `time:hasDuration`, because OWL-Time applies that property to a temporal entity, whereas an NCREM workflow is a PROV plan. |
| `ncrem:hasParameter` | Retained for model, scenario, workflow, and control-configuration inputs. It is not mapped to SAREF `hasProperty`, whose subject is a feature kind or feature of interest. |
| `ncrem:hasMaterialBank` | Retained as a broad application-profile association. Activities should use `prov:used` or `prov:generated` when the provenance role is known. |
| `ncrem:changesSetpoint` | Retained because it describes the intended effect of a recommended plan, not a completed SOSA actuation. |
| `ncrem:hasSetpoint` | Retained because the NCREM object is a SAREF property-like setpoint, not necessarily a Brick point entity. |
| `ncrem:monitors_Segment` | Retained because it links a sensor to its monitored road segment; SOSA normally expresses the feature of interest through an observation. |

The remaining local relations express mobility, sourcing, weather-file, workflow, or application-profile roles for which this release does not assert an exact external superproperty. They remain candidates for later review as the ontology’s implemented datasets and competency queries expand.
