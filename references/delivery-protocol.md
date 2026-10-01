# Shared-project delivery contract

New requests use schema version 2. Preserve old reports and use unique request/adviser basenames in the existing review directory. Only the exact named outputs are writable; directory membership does not grant access to neighboring reports.

Write the full report first, ending with the exact unique sentinel, then completion JSON last. The report includes the request ID, findings, evidence actually read, counterevidence and uncertainty. Do not silently revise it after completion.

```json
{
  "schema_version": 2,
  "request_id": "example-review-001",
  "adviser": "gemini",
  "input_manifest_sha256": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "status": "complete",
  "report_file": "example-review-001.gemini.report.md",
  "findings_file": null
}
```

Keep this controller session outside the adviser's allowlist. Paths below are illustrative, not defaults; resolve an existing canonical local directory for the current host.

```json
{
  "schema_version": 2,
  "request_id": "example-review-001",
  "adviser": "gemini",
  "input_manifest_sha256": "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef",
  "output_directory": "/absolute/project/docs/reviews",
  "report_file": "example-review-001.gemini.report.md",
  "completion_file": "example-review-001.gemini.completion.json",
  "findings_file": null,
  "findings_required": false,
  "sentinel": "GEMINI38_FLASH_HIGH_RESULT_EXAMPLE_001",
  "dispatch_state": "SENT",
  "generation_stopped": true,
  "unresolved_approval": false
}
```

The controller sets `generation_stopped` and `unresolved_approval` from current UI observations, never from the existence of completion JSON. Persist `NOT_SENT -> UNKNOWN` before Send, and `SENT` after visible submission. UNKNOWN and SENT requests must be recovered, not resent.

After observing generation stop, run the offline collector with absolute paths:

```sh
python3 scripts/collect_delivery.py --session /absolute/project/docs/reviews/example-review-001.gemini.session.json --receipt-file /absolute/project/docs/reviews/example-review-001.gemini.receipt.json --stable-seconds 1
```

On Windows use an available Python executable and equivalent resolved paths; do not assume `python3` exists. Python 3.10 or newer and the standard library suffice. This script does not contact or control the model.

The collector checks identity, strict JSON, exact allowed output basenames, final sentinel and stable bytes, then creates an integrity receipt. Only this request's outputs are read. Identical receipt retries do not rewrite anything; changed reports and conflicting/partial receipts fail. Symlinks, reparse points, hardlinks, traversal, Windows alternate streams and device names are refused. Use canonical directories: a macOS `/var` alias or other symlink ancestor may intentionally fail these checks; resolve and verify the real intended root before creating the session, rather than weakening checks.

The collector does not verify the manifest's input files, model selection, generation state, evidence access or report truth. Those remain separate controller observations. A protocol PASS never implies a factual PASS. Never rewrite adviser reports, overwrite receipts or broaden access to force acceptance.

For unavailable native file tools, preserve the same request and use supported native export/UI text to collect the complete original answer. Do not resend or ask for a model-authored reconstruction. One same-turn recovery is allowed for truncation; otherwise mark incomplete and retain the blocker. Avoid AI composers as clipboard intermediaries.

Optional findings, when declared before dispatch, use version 2 and matching identity fields plus `recommendation`, `findings`, `evidence_read`, `unknowns`. Each finding has `id`, `severity` (`info|low|medium|high|critical`), `claim`, `file` (string or null), `line` (positive integer or null), `trigger`, `evidence_kind`, `counterevidence`, `suggested_check`. No findings file is needed for a prose review.

The bundled collector retains version 1 recovery for existing sessions via `--snapshot-dir` and old fixed basenames. Use that route only for a real legacy request; do not migrate identities or resend an interrupted consultation.
