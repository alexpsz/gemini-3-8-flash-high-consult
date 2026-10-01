# Shared evidence and dispatch

Use one task packet in the project's existing review location. Include the question, audience, goals, constraints, artifact, facts, contrary evidence, known attempts, unknowns, exact permitted inputs and exact writable outputs. Allow a no-change recommendation. Keep controller rankings and other advisers' reports outside the allowlist.

Create a manifest that lists each exact input's project-relative path, byte length and SHA-256, plus the packet entry. Resolve any separately authorized external input explicitly; do not broaden a folder allowlist. Compute `input_manifest_sha256` from the **manifest's exact UTF-8 bytes**, and separately record `packet_sha256` from the packet. Recheck file hashes before dispatch. A manifest hash identifies the intended evidence; it does not prove the model read the evidence. Preserve a stable manifest and inputs for the duration of the review, or start a new identified review for changed inputs.

Scan and inspect the exact outgoing texts with `scripts/check_packet_safety.py`. Verify essential reads using content-specific references. Record unsaved editor buffers separately from disk inputs.

## Short resolved wrapper

Replace bracketed fields before sending. If native-file root binding is needed, add the marker's exact path and nonce-check instruction; never include the expected nonce in the wrapper. Require a mismatch or unreadable marker to halt substantive work in the same conversation.

```text
CONSULT_DISPATCH_V3
REQUEST_ID: [unique request ID]
ADVISER: gemini
ROOT: [controller-verified canonical absolute root]
PACKET: [absolute packet path]
PACKET_SHA256: [exact packet SHA-256]
INPUT_MANIFEST: [absolute manifest path]
INPUT_MANIFEST_SHA256: [exact manifest SHA-256]
Read the packet and only the exact manifest-listed inputs. Give an independent
first assessment. Do not read controller notes or other advisers' reports.
Product inputs are read-only. Use native file tools; no terminal execution,
installs, security changes, commits, publication or unrelated reads.
DELIVERY: files; schema_version 2
REPORT: [absolute request.gemini.report.md]
COMPLETION: [absolute request.gemini.completion.json]
FINDINGS: none
Write the complete first answer into REPORT, including REQUEST_ID, evidence
actually read, counterevidence, unknowns and access gaps. End with the exact
sentinel below. Write COMPLETION last using the specified schema and exact
report basename, then post a short notice. If native file delivery fails,
give the complete answer in this same chat; do not widen scope or resend.
FINAL_SENTINEL: [unique GEMINI38_FLASH_HIGH_RESULT_... value]
END_DISPATCH: [same request ID]
```

Supply the small completion JSON schema from the delivery reference if needed. Only authorize exact `.tmp` paths if the application supports atomic file writing and it materially helps. Do not request terminal commands to obtain atomicity.

The controller's session additionally stores requested/observed model and effort, root/revision, UI versus native-file binding evidence, conversation locator, context exposure, wrapper hash, transport and collection status. This record is not evidence for the reviewer. A later informed follow-up has its own ID and sentinel and does not count as an independent review.
