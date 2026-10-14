# CHAKRA Project Memory

## CHAKRA is the founder startup

- Type: fact
- ID: acd30912b32f472e8d03eaeec94c569a
- Created: 2026-10-14T06:35:28+00:00
- Source: Founder message, 2026-10-14
- Tags: founder-provided, startup

The founder is currently building a startup called CHAKRA. Industry, product, customers, and business model are not yet specified.

## Founder-confirmed CHAKRA focus

- Type: fact
- ID: 56d09d72330445c79fc2fa0ce8d5712a
- Created: 2026-10-14T06:51:55+00:00
- Source: Founder message, 2026-10-14
- Tags: founder-confirmed, startup, polyp, colorectal-cancer

CHAKRA is an AI-in-healthcare startup. The founder says its current focus is polyps related to colon cancer, especially colonoscopy polyp work. This confirms the startup direction, not a finalized intended-use statement or approved clinical product claim.

## ChakraModel research problem framing

- Type: note
- ID: d8c2d6c1d9204a7b94fb9f565810667e
- Created: 2026-10-14T06:52:00+00:00
- Source: Drive: ChakraModel complete technical documentation and project journey; https://drive.google.com/file/d/1jXJ7o24N6Dque4crihxptg3armJUEAzw/view ; https://drive.google.com/file/d/1DV3yBrEBIWPHMKClEyfflVQQdcm3H0Oo/view
- Tags: research, problem-framing, colonoscopy

Internal ChakraModel documents frame the research problem as polyp detection/segmentation in live colonoscopy video, especially temporal flicker, cross-device/domain shift, and end-to-end latency. The project history moves from YOLO-based detection toward a pipeline with temporal tracking and segmentation. Treat this as research framing and historical architecture, not the startup's finalized product specification.

## Documented ChakraModel implementation components

- Type: note
- ID: d090fdcfd976411f97d48c66527358f8
- Created: 2026-10-14T06:52:05+00:00
- Source: Drive: ChakraModel complete technical documentation; https://drive.google.com/file/d/1jXJ7o24N6Dque4crihxptg3armJUEAzw/view
- Tags: architecture, implementation, source-qualified

The internal forensic documentation reports a YOLOv8n detector, a 2D ByteTrack/state-machine persistence path with EMA and frame confirmation/occlusion holding, a ViT-Large ChakraTransformer segmenter, and heuristic Paris morphology labels. It says the ViT-Large model has about 309M parameters at 384x384 input; Paris labels are geometric heuristics rather than a trained clinical classifier; and the pipeline does not implement 3D SLAM. Verify these claims against the current code and checkpoint before treating them as current implementation facts.

## Do not reuse ChakraModel performance claims without provenance

- Type: lesson
- ID: 8d1190eb18ab4fdf8e4a5005d533c81b
- Created: 2026-10-14T06:52:09+00:00
- Source: Drive: ChakraModel version history and complete technical documentation; https://drive.google.com/file/d/1rgnk8iIjNKsjai36HEBT_xEKq9LNaTtj/view ; https://drive.google.com/file/d/1jXJ7o24N6Dque4crihxptg3armJUEAzw/view ; pitch draft https://drive.google.com/file/d/1Ocf_ymtNyI2dqFWxy70tpDKT0_FhFtdR/view
- Tags: validation, metrics, scientific-integrity, lesson

Internal pitch and model-comparison files claim high Dice scores, 94.7 FPS, conformal coverage, TRL 4, and regulatory status. Later internal forensic documentation says key headline metrics lack producing artifacts, describes a 0.4555 full-pipeline ablation, reports much slower YOLO+ViT latency, and flags placeholder/canary data in CVC-300 and ETIS folders. These internal reports have not been independently reproduced in this memory task. Before external use, verify the exact checkpoint, code commit, dataset version and patient/video-level split, command, hardware, and raw artifacts. Do not claim clinical efficacy, safety, SOTA, zero-miss performance, clinical readiness, or clearance from pitch material alone.

## Polyp sub-phenotype benchmark is a proposal

- Type: note
- ID: 5e9e181d900f41b3831e41e6d7e815df
- Created: 2026-10-14T06:52:15+00:00
- Source: Drive: polyp_subphenotype_benchmark_spec.md; https://drive.google.com/file/d/1b8Oe69luQBJomoKtGGIZYx7UQ6UpwS-6hG_RNfeb400/view
- Tags: benchmark, research-plan, clinical-annotation

The internal benchmark specification proposes deriving size, morphology, and boundary proxy classes from segmentation masks and evaluating them with grouped splits, leakage checks, cross-dataset analysis, and blinded clinician review. It explicitly says Paris/NICE/Kudo classes require endoscopist or pathology annotation and are not labels supplied by segmentation-only datasets. Do not describe this proposed benchmark or clinician review as completed.

## Market and regulatory research remains exploratory

- Type: note
- ID: 19e56f931baa45dc89ff7f196638df9a
- Created: 2026-10-14T06:52:18+00:00
- Source: Drive: market research https://drive.google.com/file/d/1drk2L1nhUNcd1R-SPSsZrxSN8HQvesPP/view ; domain/SaMD research https://drive.google.com/file/d/1LcbZ07jgUZHwv364k9WKc9kNcJOZsS34/view ; technical research https://drive.google.com/file/d/1kskrMCkCpgOz0uUDR1qw5_KmHyQJyHZS/view ; pitch draft https://drive.google.com/file/d/1Ocf_ymtNyI2dqFWxy70tpDKT0_FhFtdR/view
- Tags: market, regulatory, hypothesis

Internal market, domain, and technical research files discuss hospitals and ambulatory surgery centers, false-positive alert fatigue, edge integration, shadow-mode evaluation, diverse clinical data, and quality/regulatory processes. These are exploratory research outputs and recommendations, not validated customer discovery, a selected buyer/business model, a chosen regulatory route, or proof of compliance. Pitch deck market-size, regulatory-classification, TRL, and IP statements require separate primary-source validation.

## Internal research brief emphasizes systems integration

- Type: note
- ID: 1f38ae47d9e344d392936fbd6c34cbca
- Created: 2026-10-14T06:52:23+00:00
- Source: Drive: ChakraModel research brief; https://drive.google.com/file/d/1x4tQLTB5QsOv1Fya2CnK9h1ipzNPs2rx/view
- Tags: research, strategy, hypothesis

The ChakraModel research brief frames the near-term opportunity as integrating reliable detection with temporal tracking and artifact-aware processing, with careful evaluation of generalization and live-video constraints, rather than assuming a novel architecture. This is an internal research recommendation, not a confirmed startup roadmap.

## CHAKRA source coverage is account-limited

- Type: note
- ID: bc5296f082f04b158fca60570908d5e3
- Created: 2026-10-14T06:52:26+00:00
- Source: Drive profile and shared-drive list checked 2026-10-14; docs/drive-context-review.md
- Tags: source-coverage, drive

The 2026-10-14 Drive review used the connected Varsha S Rao account with the founder's teammate authorization. The connector listed no shared drives. Gokul, Girupa, and Jayasri personal Drive accounts were not connected and their files were not scanned. GitHub review is separately documented in docs/github-context-review.md.

## ChakraNet product smoke check: UI works, models not ready

- Type: note
- ID: 917df733c59e4214a1e880fb8dea92f6
- Created: 2026-10-14T06:56:12+00:00
- Source: Local repo M:\chakramodelpro-push (README identifies Gokzz-glitch/chakramodelpro); tested 2026-10-14
- Tags: product-test, readiness, model-unavailable

On 2026-10-14, read-only smoke checks of the local ChakraNet Polyp Evaluation Project returned HTTP 200 for the UI and /api/state and discovered six model entries. All six reported ready=false: five lacked local weights; the PraNet/PVT segmentation entries also lacked required model source; ChakraNet had no inference runner. Python syntax compilation passed for backend.py, video_infer.py, and both segmentation evaluators. No model inference or clinical evaluation ran because runnable weights/source were missing.

## GitHub ChakraModel repository map

- Type: note
- ID: c73484a907d640069a33edb6e6800b92
- Created: 2026-10-14T06:56:37+00:00
- Source: GitHub: https://github.com/Gokzz-glitch/chakramodel ; https://github.com/Gokzz-glitch/chakramodel/blob/main/README.md ; https://github.com/Gokzz-glitch/chakramodel/blob/main/ARCHITECTURE-SPINE.md ; https://github.com/Gokzz-glitch/chakramodel/blob/main/docs/reports/model_comparison_report.md
- Tags: github, chakramodel, source-qualified

Gokzz-glitch/chakramodel contains colonoscopy polyp detection/segmentation research, architecture proposals, notebooks, and benchmark artifacts. Its README/model-comparison report claim strong ChakraTransformer benchmark results and six model combinations; later internal Drive provenance documents conflict with those claims. Treat repository claims as self-reported until the exact artifacts and runs are independently reproduced.

## Keep ChakraModel benchmark contradictions visible

- Type: lesson
- ID: c46c5253c9ef4fe3ae240206d3a13dd2
- Created: 2026-10-14T06:56:37+00:00
- Source: GitHub: https://github.com/Gokzz-glitch/colonoscopy-ai-guide/blob/main/README.md ; https://github.com/Gokzz-glitch/colonoscopy-ai-guide/blob/main/pages/08-benchmark-integrity.html ; https://github.com/Gokzz-glitch/colonoscopy-ai-guide/blob/main/pages/09-chakramodel.html ; older source https://github.com/Gokzz-glitch/chakramodel/blob/main/README.md
- Tags: github, benchmark, provenance, lesson

GitHub ChakraModel and its colonoscopy-ai-guide integrity pages present conflicting benchmark narratives. Older repository material claims SOTA Dice and speed; the later guide reports leakage concerns and weaker results/latency. The guide's audit is also a project-authored claim, not independent validation. Preserve both sources and reproduce before publishing any metric.

## Related GitHub projects are distinct from the polyp startup focus

- Type: note
- ID: 92040b5a4a024ea191308a8f108b8c13
- Created: 2026-10-14T06:56:38+00:00
- Source: GitHub: https://github.com/Gokzz-glitch/chakramodelpro/blob/main/README.md ; https://github.com/Gokzz-glitch/Chakra-pulse/blob/main/README.md
- Tags: github, project-boundaries, hypothesis

Gokzz-glitch/chakramodelpro describes a Phase 0 literature-review effort and labels its lightweight temporal hybrid direction as a working hypothesis. Gokzz-glitch/Chakra-pulse concerns blood logistics/immunohematology and is a separate healthcare project; do not merge it into CHAKRA's current colonoscopy-polyp context without founder confirmation.

## Spreadsheet is a squad tracker, not a CHAKRA product specification

- Type: note
- ID: acc32019b4a64982accb32e23762000c
- Created: 2026-10-14T08:19:19+00:00
- Source: Founder-shared Google Sheet: BRAIN ROTZ; dashboard A1:Z15; https://docs.google.com/spreadsheets/d/1SPunf_GOmpBif-hrCJ5BDf39Dh4H40nme5RgxtI5WsE/edit ; reviewed 2026-10-14
- Tags: spreadsheet, team-context, scope-caveat

The BRAIN ROTZ workbook covers a four-person squad (Gokul, Girupa Shankar V, Jayasri, and Varsha S Rao) and mixes GATE study, job readiness, and ML tasks. Some entries are relevant to CHAKRA's polyp research, but the workbook is not a finalized product specification or authoritative live status source.

## Threshold validation task is listed as open in the team tracker

- Type: note
- ID: 340949b674ba40879f28a1f659309e55
- Created: 2026-10-14T08:19:19+00:00
- Source: Founder-shared Google Sheet: BRAIN ROTZ; ✅ TASK TRACKER A1:L34; Jayasri/Girupa/Varsha daily-task tabs A1:L30; reviewed 2026-10-14
- Tags: polyp, validation, thresholds, team-tracker, reported-not-verified

The master task tracker lists a high-priority task for Jayasri to test app models at thresholds 0.4, 0.5, 0.6, and 0.7 against Girupa's dataset, consulting Varsha. It is marked Not Started with due text 'End of this week'; the sheet does not establish a calendar due date or confirm whether this remains current. Confirm model/checkpoint, dataset identity and split, owner, and reporting artifact before treating it as an active execution plan.

## Team spreadsheet reports dataset preparation work that needs artifact verification

- Type: note
- ID: 2b3de9c9d8d3458e962f91c7a9a0f3fa
- Created: 2026-10-14T08:19:19+00:00
- Source: Founder-shared Google Sheet: BRAIN ROTZ; 👤 GIRUPA - DAILY TASKS A1:L30; 👤 VARSHA - DAILY TASKS A1:L30; ✅ TASK TRACKER A1:L34; reviewed 2026-10-14
- Tags: datasets, polyp, video, status-conflict, reported-not-verified

Girupa's daily task tab reports dataset cleaning V4 as Finished, hashing a combined 800+ GB dataset as not started, classification of about 14,000 images using Varsha's report as In Progress, video duplicate checks and PolypGen cleanup as not started, and 'real colon 880gb extraction' as Finished while 24-class and 5-class splits appear incomplete. Varsha's tab marks some video model comparison/student-teacher work Finished even while master tracker entries leave related benchmark work Not Started. These are conflicting team-reported statuses, not independently verified dataset measurements or completed model results.

## Spreadsheet lists candidate polyp-video sources without provenance confirmation

- Type: note
- ID: 6324278c06b944fe968d65d8211035af
- Created: 2026-10-14T08:19:19+00:00
- Source: Founder-shared Google Sheet: BRAIN ROTZ; Sheet3 A1:L15; Dataset & Resource Hub A1:N40; reviewed 2026-10-14
- Tags: datasets, colonoscopy, video, provenance, reported-not-verified

The video-resource tab lists LDPOLYP videos with polyps, LDPOLYP videos without polyps, Hyper-Kvasir videos, INFODB, and CAS-COLON. Listing these sources does not confirm the team has obtained, licensed, cleaned, deduplicated, or validated them. The reviewed workbook does not establish patient/video-level splits, provenance, data quality, model metrics, or clinical performance.

## Treat squad spreadsheet statuses as inconsistent snapshots

- Type: lesson
- ID: cd952cf48b834d45858a55e26e861d6f
- Created: 2026-10-14T08:19:19+00:00
- Source: Founder-shared Google Sheet: BRAIN ROTZ; dashboard A1:Z15; ✅ TASK TRACKER A1:L34; member daily-task tabs A1:L30; reviewed 2026-10-14
- Tags: lesson, status-integrity, planning, team-tracker

When using BRAIN ROTZ for CHAKRA planning, do not rely on its dashboard counters alone: dashboard totals, master tracker, and individual daily tabs disagree on completion. Confirm the task owner, current dataset/model artifact, and evidence before carrying a status into a plan or external claim.
