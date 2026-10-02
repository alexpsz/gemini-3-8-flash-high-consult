# Evidence and dispatch

Reuse one neutral packet in the owning project's existing review location, normally `docs/reviews`. Include the question, goals, constraints, actual artifacts, counterevidence, unknowns and exact local read/write allowlists. Relevant public web research is additionally permitted by default; record any explicit offline or narrower source restriction. Exclude previous verdicts and neighboring reports; permit no-change conclusions. Record harness/project-memory exposure as observed or unknown. A new conversation does not establish isolation.

Manifest entries contain exact project-relative path, byte length and SHA-256; explicitly resolve authorized external inputs. Hash manifest UTF-8 bytes separately from packet bytes. Check inputs once before dispatch and again only if they may have changed. Keep them stable through review; changed evidence after submission requires a separately identified review. Use authoritative source bytes. For external inputs without an existing native read grant, stage exact authorized copies under the owning project review directory and retain original source paths and hashes; do not recapture unchanged generated evidence. Unsaved buffers are separate evidence.

Run `scripts/check_packet_safety.py` on exact outgoing texts and inspect them. The scanner is heuristic. Remove secrets only from outgoing copies; omit unrelated private history, raw media and credentials.

Resolve every bracketed field. For CLI, prefer bounded evidence directly in the prompt when sufficient; include paths/hashes and label inline excerpts. For that route, replace the file-reading block below with the actual inline evidence and remove unused packet/manifest paths; make no tool-read claim. Otherwise use the file-access block. Keep the packet marker out of the wrapper so a later echo can corroborate an actual read. One marker never proves every input was read.

```text
CONSULT_DISPATCH_V4
REQUEST_ID: [unique request ID]
ADVISER: gemini
ROOT: [approved canonical absolute root]
PACKET: [absolute packet path]
PACKET_SHA256: [packet hash]
INPUT_MANIFEST: [absolute manifest path]
INPUT_MANIFEST_SHA256: [manifest hash]
For file-based evidence, first read only PACKET with the available file tool. If unreadable or its binding
marker is missing, stop. Echo its marker and one content fact, then continue;
the controller will corroborate these later, not approve a preliminary gate.
Read the manifest and only its exact local inputs. Give an independent first
assessment. Do not read controller notes or other advisers' reports.
Product files are read-only. No terminal commands, installs, security changes,
commits, publication or unrelated access.
Relevant public web search and page reading are permitted by default. Use
search_web and read_url_content when useful without asking for a separate
instruction. Honor explicit offline or narrower source limits in this request.
If your web tool saves its response to a local file, reading that exact response
file under this conversation's .system_generated/steps directory with view_file
is part of authorized web research, in addition to the manifest's local inputs.
Do not traverse other conversations. Read the actual saved content before citing
it; a wrapper title such as Live Content is not the webpage's actual title.
Cite sources actually accessed and distinguish them from packet evidence.
Keep private inputs out of unnecessary search queries. Do not submit forms,
post or interact with accounts. Report denied tools and missing evidence;
do not repeat the same rejected action or claim a denied source was read.
DELIVERY: complete final response; controller captures stdout
Return the complete first answer, request ID, evidence actually read,
counterevidence, uncertainty and access gaps. Do not create report or completion
files. End with the exact sentinel as the last line of plain text, without quotes, code fences or Markdown formatting. The controller preserves your full answer.
FINAL_SENTINEL: [unique GEMINI38_FLASH_HIGH_RESULT_... value]
END_DISPATCH: [same request ID]
```

For native fallback only, replace DELIVERY with `files; schema_version 2`, name exact REPORT/COMPLETION paths, and supply the schema from [delivery](delivery-protocol.md). Require report first, completion last, and full in-conversation output if file delivery fails. Authorize exact temporary paths only for supported native atomic writes, never terminal commands. Use [native workflow](native-workflow.md) for project/file corroboration. Preserve the first answer before informed follow-up; follow-ups have distinct IDs and do not count as independent reviews.

The runner validates a file-based `INPUT_MANIFEST` automatically before launch. Its JSON object uses `root` and `inputs`; each input has `project_relative_path` or `absolute_path`, `bytes`, `sha256`, and optional `role`/source provenance. See [runtime checks](runtime-recovery.md) before dispatching external screenshots.
