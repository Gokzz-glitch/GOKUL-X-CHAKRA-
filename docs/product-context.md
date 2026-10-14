# CHAKRA product context

## Founder-confirmed direction

- CHAKRA is an AI-in-healthcare startup.
- Its current focus is polyp-related colon cancer work, especially colonoscopy polyp detection and segmentation.
- Source: founder message, 2026-10-14.

## GitHub project map

- `Gokzz-glitch/chakramodel` contains colonoscopy polyp detection/segmentation research, multiple model variants, training notebooks, and evaluation artifacts.
- `Gokzz-glitch/chakramodelpro` describes a separate research pipeline in an early literature-review phase and lists real-time, cross-dataset generalization as a working hypothesis.
- `Gokzz-glitch/colonoscopy-ai-guide` is an education and research site with a ChakraModel overview and a benchmark-integrity audit.
- `Gokzz-glitch/GOKUL-X-CHAKRA-` is the private startup workspace used for this memory project.
- `Gokzz-glitch/Chakra-pulse` is a different healthcare project about blood logistics and immunohematology; do not treat it as the current polyp product without founder clarification.

## Drive/GitHub research context

- Drive documentation frames the ChakraModel research problem as temporal instability in colonoscopy video, cross-device/domain shift, and end-to-end latency. See [Drive context review](drive-context-review.md) for source-attributed implementation notes and metric conflicts.
- The documented pipeline history includes YOLOv8 detection, 2D tracking/persistence, polyp segmentation, and heuristic morphology. Technical documents also describe a ViT-Large segmenter, but its runtime and validation limitations are material.
- The benchmark specification proposes segmentation-mask-derived sub-phenotype proxies and grouped/leakage-resistant evaluation. It explicitly reserves Paris/NICE/Kudo labels for clinician/pathology annotation; this is a proposed research plan, not a completed clinical benchmark.
- Drive pitch and interview files include aspirational claims that conflict with later provenance audits. Keep all metrics, regulatory statements, TRL labels, and clinical claims marked as unverified until reproduced or confirmed.
- Drive review coverage currently includes only the connected Varsha account, with the founder's authorization. Gokul, Girupa, and Jayasri account contents remain unreviewed until those accounts are connected.

## Evidence quality and open questions

- Older ChakraModel README/report files claim strong benchmark results and a research-paper submission.
- The later colonoscopy-ai-guide audit describes benchmark leakage and reports substantially weaker ChakraTransformer performance and latency. These are conflicting project-authored claims, not independently reproduced results.
- Preserve model/checkpoint, dataset split, metric, hardware, and source whenever recording a result. Do not use the older SOTA or clinical-safety claims in a pitch or clinical claim until reconciled against reproducible runs.
- The reviewed material establishes a research direction, not regulatory clearance, clinical validation, or a finalized product specification.
- A read-only smoke check of the local [ChakraNet Polyp Evaluation Project](https://github.com/Gokzz-glitch/chakramodelpro) returned HTTP 200 for both the UI and `/api/state` and discovered six model entries. All six reported `ready: false`: five lacked local weights (the segmentation entries also lacked required model source; ChakraNet had no inference runner). Python syntax compilation passed for the backend, video runner, and two segmentation evaluators. No model inference or clinical evaluation was run because runnable weights/source were unavailable.

## Not yet established

The target user, clinical workflow, intended-use statement, buyer, business model, deployment setting, and regulatory strategy remain open until the founder confirms them.
