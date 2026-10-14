# Squad spreadsheet context review

Reviewed read-only on 2026-10-14 from the founder-shared Google Sheet [BRAIN ROTZ](https://docs.google.com/spreadsheets/d/1SPunf_GOmpBif-hrCJ5BDf39Dh4H40nme5RgxtI5WsE/edit). No cells were edited.

## Workbook scope

The dashboard describes a four-person squad (Gokul, Girupa Shankar V, Jayasri, Varsha S Rao) focused on GATE 2026/2027 mastery and industry ML/AI job readiness. It organizes master tasks, individual daily-task and resource-intake tabs, dataset/resources, ML progress, daily allocations, and activity logs. This is broader than CHAKRA and includes GATE, DSA, career preparation, and unrelated study resources; those were not imported as startup context.

## CHAKRA-relevant work and dataset context

- The master tracker has a high-priority task for Jayasri to test app models at thresholds 0.4, 0.5, 0.6, and 0.7 against Girupa's dataset, consulting Varsha. It is marked Not Started with due text “End of this week”; this sheet does not establish a calendar due date or confirm that it remains current.
- Girupa's daily tab tracks dataset cleaning/version 4, hashing a combined 800+ GB dataset, classification of about 14,000 images using Varsha's report, video-dataset duplicate checks, and PolypGen cleanup. It marks “real colon 880gb extraction” Finished, while splitting into 24- and 5-class versions appears incomplete/false. These are team-reported tracker entries, not independently verified measurements or dataset contents.
- Varsha's daily tab marks video-model comparison work and testing a student-teacher model on a video dataset Finished, while a separate master task still marks model benchmarking/training/testing Not Started. A positive/negative-ratio and threshold test appears Not Started in both the master tracker and daily-task material.
- Gokul's daily tab lists preparing a clean model for a presentation to “Gladys mam” as Not Started (dated 2026-10-13). Whether this is a CHAKRA deliverable is not explicit.
- The video resource tab lists LDPOLYP videos with polyps, LDPOLYP videos without polyps, Hyper-Kvasir videos, INFODB, and CAS-COLON as possible video dataset sources. Listing a source does not confirm that the team has downloaded, licensed, cleaned, or validated it.

## Status and data-quality caveats

The dashboard summarizes 31 master tasks with 0 completed and 3 in progress, while individual daily tabs contain rows marked Finished/TRUE. The master tracker also differs from personal tabs on model/video test completion. Treat statuses as an inconsistent snapshot rather than a definitive live project state; check the task owner and current artifact before updating a plan. The daily allocation shows no active slots, and the activity log reports zero events in the ranges reviewed.

The Dataset & Resource Hub primarily lists general study and ML resources. It should not be treated as a complete polyp-data inventory. The workbook itself does not provide enough evidence to confirm dataset provenance, patient/video-level splits, licensing, data quality, model metrics, or clinical performance.

## How to use this context

Use the threshold test against Girupa's dataset as a candidate open validation task, but confirm its owner, current status, dataset identity/split, and reporting artifacts before execution. Keep the large-dataset, class-splitting, duplicate-check, and student-teacher video items marked as spreadsheet-reported activity until evidence is linked. Do not let this study/workforce tracker override the product-status findings in [product context](product-context.md) or the source-integrity cautions in [Drive review](drive-context-review.md) and [GitHub review](github-context-review.md).

## Source ranges reviewed

- Dashboard overview and squad scope: `📊 DASHBOARD` A1:Z15.
- Master work items: `✅ TASK TRACKER` A1:L34.
- Member work entries: `👤 GOKUL - DAILY TASKS`, `👤 GIRUPA - DAILY TASKS`, `👤 JAYASRI - DAILY TASKS`, and `👤 VARSHA - DAILY TASKS` A1:L30.
- Resource intake: `📁 DATASET & RESOURCE HUB` A1:N40.
- Video-source list: `Sheet3` A1:L15.
- Current allocation and log counters: `🗓️ DAILY WORK ALLOCATION` A1:L35 and `📋 ACTIVITY LOG` A1:L30.
