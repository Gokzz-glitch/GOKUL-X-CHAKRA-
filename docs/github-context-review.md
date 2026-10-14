# GitHub context import notes

Reviewed 2026-10-14. These are repository-authored summaries; they are not independent medical, regulatory, or benchmark validation.

## Relevant repositories

- `chakramodel`: polyp detection/segmentation research. The README describes six model combinations and reports strong CVC-ClinicDB and ETIS-Larib results for ChakraTransformer.
- `chakramodelpro`: a separate polyp-research project. Its README calls the work Phase 0 (literature review) and labels its real-time hybrid-model idea a working hypothesis.
- `colonoscopy-ai-guide`: public/patient education plus research integrity site. Its pages describe leakage in standard dataset splits and report an earlier ChakraTransformer result of 0.771 Dice on CVC-ClinicDB and 7.76 FPS, in tension with the older model README/report.
- `GOKUL-X-CHAKRA-`: private project repository.
- `Chakra-pulse`: separate blood-logistics and immunohematology project; excluded from the current polyp product context.

## Reconciliation rule

Keep the benchmark discrepancy explicit. Before using any metric externally, identify the exact checkpoint, split, dataset version, code commit, hardware, and evaluation command and reproduce it. The integrity site also makes its own audit claims; treat those as project-reported findings until independently reproduced.

## Sources

- https://github.com/Gokzz-glitch/chakramodel/blob/main/README.md
- https://github.com/Gokzz-glitch/chakramodel/blob/main/ARCHITECTURE-SPINE.md
- https://github.com/Gokzz-glitch/chakramodel/blob/main/docs/reports/model_comparison_report.md
- https://github.com/Gokzz-glitch/chakramodelpro/blob/main/README.md
- https://github.com/Gokzz-glitch/colonoscopy-ai-guide/blob/main/README.md
- https://github.com/Gokzz-glitch/colonoscopy-ai-guide/blob/main/pages/08-benchmark-integrity.html
- https://github.com/Gokzz-glitch/colonoscopy-ai-guide/blob/main/pages/09-chakramodel.html
- https://github.com/Gokzz-glitch/Chakra-pulse/blob/main/README.md