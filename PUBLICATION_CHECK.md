# Public CLI update — v0.2.0

This prerelease packages the official CLI consultation route, per-turn default web permissions, bounded receipts and recovery, and fixed user-session runtime profiles. Native Windows adds a locally generated SID-bound profile and direct native executable dispatch; the existing macOS profile remains compatible.

Public files use generic paths and synthetic session identifiers. Private runtime profiles, authentication stores, caches, consultation streams, screenshots, product evidence and upgrade backups are excluded. Runtime profiles must be generated on each target machine. Preserve the bundled license and source attribution.

The automated offline-check workflow runs synthetic helper tests on Windows and macOS. Check the workflow results for the exact commit being installed. Those checks do not authenticate either CLI, send a live review, or prove web access on another account or laptop. Release notes distinguish offline validation from live consultation evidence.

The historical records below describe their respective earlier snapshots and are not assertions that the current Windows live workflow has been accepted.

# CLI-first revision — 2026-10-01

New consultations now use the signed-in official CLI with the normal harness and skills. The added single-shot runner records raw streams and controller receipts independently of the existing native file-delivery protocol. Native UI recovery remains available for its existing conversations.

Live synthetic protocol probes were completed on macOS with Claude Code 2.1.286 (10.554 seconds) and Antigravity CLI 1.2.14 (20.608 seconds). Both read the specified fixture, returned its marker, identified its deliberate calculation defect, emitted a complete native final answer and exited 0. Claude native metadata identified Opus 5.5; Antigravity identified Gemini 3.8 Flash High. Effective effort and Ultracode workflow state were not exposed, so those settings remain requested/configured rather than verified. These are small single-run observations, not a general speed benchmark or proof that every configured skill/plugin works. The CLI probes do not establish autonomous native desktop reliability.

The new runner is verified using subprocess fixtures and offline replay of the preserved live streams. Final test and installation receipts belong to the controller's upgrade record; do not infer them from this historical publication checklist.

## Historical native release checks

The material below records earlier revisions and their test scopes. Earlier statements that no live consultation was sent apply to those revisions, not the CLI probes above.

# Local workflow upgrade — 2026-10-01

This update shortens the native workflow, reuses valid observations, bounds recovery, and adds offline checkpoint/CAS management and create-only original-byte archives. The current macOS offline suite passes 96 tests, including dispatch ambiguity, typed partial observations, UI conflicts, independent adviser checks, archive retries and changed-source recovery. Skill structure validation passes. Installation and rollback are separately verified by the controller.

An earlier macOS consultation produced real files with manual assistance. Autonomous model selection, text entry and send remain unverified; this upgrade does not claim to repair native control or measure live speed gains. The native route is retained; no new consultation was submitted for these tests.

## Historical release validation

The records below apply to earlier package snapshots, not the current update.

# Publication check

## v0.1.1 dispatch-state correction

The collector previously classified every non-SENT value as `NOT_SENT`, which could make an uncertain send look definitely unsent. It now returns `DISPATCH_UNKNOWN` with the original `dispatch_state: UNKNOWN`, keeps the existing `NOT_SENT` code for a known unsent request, and rejects non-string or unrecognized states with `INVALID_SESSION_SCHEMA`. No automatic dispatch, resend, session rewrite or broader collection access was added. Existing path, identity, sentinel, stable-byte and receipt checks remain in force.

The regression tests exercise known unsent, unknown, sent and invalid states, including CLI output, unchanged session bytes, absent receipts and no output reads before the state gate. On Windows with Python 3.12.14, `python -m unittest discover -s tests -v` passed all 63 tests for this patch. This validates the local collector behavior only; it does not establish a new live macOS consultation or native UI result. No consultation was sent as part of this correction.

Scope: standalone public skill package. No live consultation was sent during this packaging review. The installed source skill was not edited. No personal project artifacts, conversation exports, account credentials, native runtime or application binaries are included.

## Changes made for this release

- Removed private host paths, private project examples, versioned plugin cache paths, historical session records and host-specific assertions.
- Replaced Windows-only routing with current-host capability discovery. macOS automation must be established by the installed native tool's documentation; there is no invented macOS `sky` compatibility claim.
- Replaced unbounded project-path navigation with one recovery or a constrained native-file marker check, explicitly distinguishing UI root verification from exact file access.
- Kept Gemini-specific model verification. No Claude effort-menu instructions or another app's recovery actions are used.
- Separated packet and manifest hashes. The manifest identifies exact inputs; the collector's report-integrity PASS is not evidence that the model read them.
- Fixed case-variant output/controller path overlap in the v2 collector for common case-insensitive macOS filesystems, with platform-independent regression cases.
- Moved tests to `tests/`, resolved temporary paths before strict link checks, added MIT licensing and public installation instructions.

## Executed checks

Windows, Python 3.12.14: all 61 tests passed with `python -m unittest discover -s tests -q`. No model, network or application calls occur in these tests.

Coverage includes synthetic credential patterns without echoing values, UTF-8/error handling, JSON identity and duplicate keys, exact shared-directory allowlists, unknown/not-sent and active-generation states, missing sentinels, concurrent file changes, create-only receipts, changed-report conflicts, traversal, alternate streams/device names, symlink and hardlink refusal, and case-variant controller/output overlap.

The outgoing documentation and UI metadata passed the credential scanner with zero findings. Test strings are deliberately synthetic credential-shaped fixtures, assembled in code; they are not real secrets. A manual package review checked that filenames and text contain no source user's identity, contact details, private paths, project history or session locators.

The initial skill-creator validator attempt lacked PyYAML; the release controller supplied that dependency in a temporary validation directory outside this package. Its final validator result is recorded separately by the release controller. `tests/test_package_structure.py` also checks this package's limited scalar frontmatter, required names/lengths, relative links and quoted Codex metadata. This is a narrow structural check, not certification or a general YAML parser. The design was checked against the [Agent Skills specification](https://agentskills.io/specification).

## Interaction scenarios reviewed

These are instruction-level walkthroughs, not live desktop execution.

| Scenario | Required outcome |
| --- | --- |
| The new conversation selects a lower thinking level | Reopen the current picker and verify Gemini 3.8 Flash plus High before sending; do not infer from a Fast badge. |
| macOS exposes no supported native control | Preserve a portable packet and report NOT_SENT; do not call a Windows runtime or substitute web/API access. |
| Project picker shows only a basename | One bounded path inspection, or exact nonce-bearing native file access with UI root still marked unverified; no Explorer/Finder loop. |
| Marker is unreadable or mismatches | Halt substantive reads and report unresolved scope in the same conversation. |
| Send times out | Keep UNKNOWN; inspect the same conversation, never duplicate the dispatch. |
| Adviser writes completion while still generating | Keep protocol acceptance pending until current UI shows stopped generation and no approval request. |
| File writes fail after submission | Collect the complete original same-turn chat answer, with no resend or model reconstruction. |
| Report or receipt path is a link or aliases a controller file | Collector rejects without overwriting target content. |
| Another reviewer writes neighboring files | Read only the exact named outputs; do not ingest that review. |
| Model asks to change product code or permissions | Stop or decline the out-of-scope action; retain evidence and original user work. |
| Private source artifact is available nearby | Explicit read allowlist applies; folder membership is not authorization to disclose it. |

## Remaining limits

Live macOS interaction, native file delivery on macOS, current account-specific model access, and a complete new consultation were not tested by this release. Application platform support in the [official Antigravity documentation](https://www.antigravity.google/docs) does not imply native automation compatibility. A successful offline check proves the tested helper behavior only. Privacy scanning remains heuristic and must be paired with inspection of each real outgoing packet.

## Final publisher validation

The bundled skill-creator `quick_validate.py` passed on the final package after its PyYAML dependency was supplied outside the package. Requirements are in the body for compatibility with older validators; the package retains valid Agent Skills frontmatter. Independent instruction-level interaction review found no blocking issue. This does not establish live native/browser behavior on macOS or a marketplace certification.
