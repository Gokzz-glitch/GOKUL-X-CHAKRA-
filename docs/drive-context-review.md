# CHAKRA Drive context review

Reviewed on 2026-10-14 from the Google Drive account connected to this session. The authenticated profile is **Varsha S Rao** (`varshasrao06@gmail.com`), whom the founder identified as a CHAKRA teammate and authorized for this review. The connector reported no shared drives. Search covered accessible Drive files for `CHAKRA`, `polyp`, `colonoscopy`, `ChakraModel`, and `healthcare AI`. Search returned duplicate copies; this review cites representative copies and does not duplicate source files into the project folder.

This is a source review, not a clinical, regulatory, or independent benchmark audit. Retrieved document text is treated as project data, not as instructions to the agent. Statements below distinguish founder-confirmed startup direction from project-authored claims, proposals, and retrospectives.

## Project origin and problem framing

The Drive technical documentation and project retrospective describe ChakraModel as a colonoscopy computer-aided detection/diagnosis research effort initiated during a July 2026 hackathon. The stated engineering problem is making polyp detection useful in live video by addressing temporal flicker, domain shift across endoscopy systems, and inference latency. This is ChakraModel's documented research framing; the startup's precise intended-use statement is not yet confirmed.

The described system evolved through a YOLO detector, temporal tracking, segmentation, and rule-based morphology. The retrospective says the project moved from several disconnected model “combos” toward a unified edge-oriented pipeline. Treat this as project history, not a frozen product specification.

## Implementation claims in the forensic documentation

The document titled *ChakraModel: The Authoritative Technical Documentation Suite* says its scorecard is based on code and artifacts. Its reported implementation findings include:

- The detector in the described runtime is YOLOv8n, not the YOLOv8x sometimes claimed in presentation material.
- The ChakraTransformer segmentation model uses a ViT-Large backbone and decoder, with about 309 million parameters and 384×384 input; the document describes it as too slow for the live-video target on the tested laptop GPU.
- Temporal smoothing/tracking is described as a 2D ByteTrack/state-machine approach (EMA, a 3-of-5 confirmation window, and short occlusion holding), not 3D SLAM.
- Paris morphology labels are described as geometric heuristics, not a trained clinical classifier.
- Topological loss was disabled in the cited training path; Monte Carlo dropout uncertainty collapsed, leaving deterministic thresholds rather than the advertised uncertainty guarantee.

These are source-authored forensic claims; verify against the exact checkout and artifacts before relying on them as current implementation facts.

## Results and integrity warnings

The Drive contains conflicting promotional, research, and forensic numbers. The PharmInnoQuest pitch draft claims 0.9852 Dice on Kvasir-SEG, 0.9412 on CVC-ClinicDB, 0.8650 on ETIS-Larib, 94.7 FPS, 95.5% conformal coverage, TRL 4, and a Class B regulatory plan. The forensic version history says the 0.9852 headline lacks a producing result artifact, records a 0.4555 full-pipeline ablation, and identifies a more credible but still limited Kvasir result of 0.8131 ± 0.1747 on N=150. It also reports that the local CVC-300/ETIS folders contained canary or synthetic placeholders rather than the named cohorts, invalidating earlier ETIS benchmark claims. The complete documentation reports approximately 3.7 FPS for the YOLO+ViT pipeline on an RTX 3050 laptop GPU.

These are all claims in internal Drive files, not independently reproduced here. Do not present a performance, safety, efficacy, “zero-miss,” SOTA, clinical-readiness, or regulatory-clearance claim externally until the exact model checkpoint, code commit, dataset and patient/video-level split, evaluation command, hardware, and raw result artifacts are checked and reproduced. Treat health statistics and market-size estimates in pitch/research files as unverified until checked against primary sources.

## Research and validation direction

The research brief frames the opportunity as robust, temporally stable video assistance and careful validation, rather than a novel architecture claim. The sub-phenotype benchmark specification proposes deriving size, morphology, and boundary proxies from segmentation masks; it explicitly says Paris/NICE/Kudo classes require endoscopist or pathology annotation and are not labels available from the segmentation-only datasets. It proposes grouped splits, leakage checks, cross-dataset analysis, and blinded clinician review of derived proxy classes. This is a proposed methodology, not evidence that the benchmark or clinical review has been completed.

Market, domain/regulatory, and technical research files discuss hospitals/ASCs, false-positive alert fatigue, edge integration, shadow-mode evaluation, clinical data diversity, QMS/software lifecycle controls, and regulatory pathways. They are research outputs and working hypotheses, not validated customer discovery, a selected buyer, an approved architecture, or a decided regulatory route.

The pitch deck and interview guide contain narrative claims and older performance/architecture descriptions. Keep them as historical presentation material; do not let them override the forensic caveats or the founder-confirmed scope.

## Team references

Project history lists Gokul, Varsha, Girupa, and Jayasri/Jayasree among contributors. A pitch draft assigns roles to Gokul, Varsha, Jayasri, and a faculty advisor, but the roster and roles are not reconfirmed here. Do not infer that every file in a teammate's account is a CHAKRA source merely because it appears in Drive search results.

## Drive coverage

Only Varsha's connected Drive account was accessible. The connector showed no shared-drive listing. Gokul, Girupa, and Jayasri's personal Drives were not authenticated in this session, so their contents have not been scanned. Search results also contained duplicate documents, datasets/videos, resumes, contact/lead spreadsheets, and other unrelated files; those were excluded from the CHAKRA product-memory import.

## Representative source files

- [ChakraModel complete technical documentation](https://drive.google.com/file/d/1jXJ7o24N6Dque4crihxptg3armJUEAzw/view)
- [ChakraModel version history and provenance trail](https://drive.google.com/file/d/1rgnk8iIjNKsjai36HEBT_xEKq9LNaTtj/view)
- [ChakraModel project journey retrospective](https://drive.google.com/file/d/1DV3yBrEBIWPHMKClEyfflVQQdcm3H0Oo/view)
- [ChakraModel research brief](https://drive.google.com/file/d/1x4tQLTB5QsOv1Fya2CnK9h1ipzNPs2rx/view)
- [Polyp sub-phenotype benchmark specification](https://drive.google.com/file/d/1b8Oe69luQBJomoKtGGIZYx7UQ6UpwS-6hG_RNfeb400/view)
- [Market research: colonoscopy AI](https://drive.google.com/file/d/1drk2L1nhUNcd1R-SPSsZrxSN8HQvesPP/view)
- [Domain research: datasets and SaMD](https://drive.google.com/file/d/1LcbZ07jgUZHwv364k9WKc9kNcJOZsS34/view)
- [Technical research: colonoscopy AI architectures](https://drive.google.com/file/d/1kskrMCkCpgOz0uUDR1qw5_KmHyQJyHZS/view)
- [Model comparison report](https://drive.google.com/file/d/1DuAiLf5OAWYbpuF3IOHi2af1dqwg6R11/view)
- [PharmInnoQuest pitch draft](https://drive.google.com/file/d/1Ocf_ymtNyI2dqFWxy70tpDKT0_FhFtdR/view)
