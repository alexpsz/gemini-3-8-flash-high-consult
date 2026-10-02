# Delivery and controller state

## CLI delivery

The [CLI helper](cli-workflow.md) captures the provider's original stream and answer, then writes controller receipt `run.json`. Preserve that run directory unchanged before synthesis or follow-up. Check `dispatch_state`, `delivery_status` and `target_verification` separately; complete text is not proof of effective effort, input access or factual correctness. Report `CONFIGURED` as configured, not verified. Retain partial/error output and its access limitations.

The helper's receipt is not an adviser-authored completion object. Do not manufacture `*.completion.json`, claim the native collector passed, or run `collect_delivery.py` on CLI output. Native session files and their current/history schema below remain for the native route only; do not merge them with CLI `run.json` or reset a native `UNKNOWN`/`SENT` to launch CLI.

## Native file delivery

Use unique request/adviser basenames; only named outputs are writable. Report first, completion last; no silent revision afterwards.

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

Keep controller state outside the adviser's allowlist. Collector fields:

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
  "dispatch_state": "NOT_SENT",
  "generation_stopped": false,
  "unresolved_approval": true
}
```

## Native current state, historical evidence

One writer maintains `controller_state.current` using `scripts/consult_state.py`; replacement moves superseded state into history (latest 25). Inspect multiple sessions together without reading reports:

```sh
python3 scripts/consult_state.py inspect --session /absolute/project/docs/reviews/example-review-001.gemini.session.json
python3 scripts/consult_state.py update --session /absolute/project/docs/reviews/example-review-001.gemini.session.json --event-file /absolute/controller-event.json
```

An update event contains `expected_sha256` from inspect's `sha256`, unique `event_id`, timezone-aware `observed_at` and complete replacement `current`. Initial legacy conversion requires `migrate_legacy: true`; never shallow-merge old blockers. `current` requires `phase`, `dispatch_state`, `generation_stopped`, `unresolved_approval`, `input_access_verified`, `input_access_status`. Optional fields are `blocker`, `next_check_at`, `recovery_count`, `conversation_locator`, `submission_observed`, `controller_send_attempted`, `ui_evidence_conflict`, `evidence`. Phases use lowercase snake_case; `manual_handoff` requires UNKNOWN and `controller_send_attempted: false`; SENT requires observed submission and a conversation locator.

Input status is `unknown|partial|verified|unavailable`; its verified flag is boolean, true only for `verified`. Each `evidence` item requires matching `adviser`, absolute session path in `session`, timezone-aware `observed_at` and `source`. Add input path, observation kind, context/revision, selected model/effort, wrapper fidelity and approval scope there. Separate UI-root binding, file corroboration, controller approvals and adviser-tool approvals; unresolved/unknown approvals keep the aggregate flag true. Counts do not prove specific files read. Keep cross-adviser scheduling/summary outside these evidence lists. File-update time is not observation time.

`NOT_SENT -> UNKNOWN` precedes controller send or manual handoff; `SENT` requires observed submission. Never reset UNKNOWN/SENT to retry. Completion requires stopped generation, no unresolved approval, original complete answer and final nonempty sentinel. Resolve conflicting UI evidence as described in [native workflow](native-workflow.md); completion JSON alone cannot establish UI state.

## Collect and preserve native delivery

After current completion observations, use Python 3.10+ and canonical absolute paths:

```sh
python3 scripts/collect_delivery.py --session /absolute/project/docs/reviews/example-review-001.gemini.session.json --receipt-file /absolute/project/docs/reviews/example-review-001.gemini.receipt.json --stable-seconds 1
```

Use the available Python command on Windows. Schema 2 verifies identity, strict JSON, named outputs, sentinel and stable bytes. It preserves original bytes in sibling `<receipt-file>.archive`, writing `.archive-receipt.json` last; optional `--archive-dir` selects another absolute directory. Keep archives outside the adviser allowlist. Identical retries recover; changed files and partial/conflicting archives fail without overwrite. Canonicalize paths before session creation: symlinks/reparse points, hardlinks, traversal and macOS `/var` aliases may be refused.

`NOT_SENT` and `DISPATCH_UNKNOWN` failures describe dispatch state, never permission to resend. Protocol PASS does not verify inputs read, model identity, UI state or factual claims. Do not rewrite reports, weaken checks or broaden access for PASS. Preserve original bytes before an informed follow-up.

If native files fail, collect the complete original turn through supported UI/export. One recovery may expand a truncated turn; otherwise retain an incomplete result. Never ask for reconstruction or use another AI composer as clipboard.

Optional predeclared findings use matching version/identity plus `recommendation`, `findings`, `evidence_read`, `unknowns`. Each finding has `id`, `severity` (`info|low|medium|high|critical`), `claim`, `file`, `line`, `trigger`, `evidence_kind`, `counterevidence`, `suggested_check`; file/line may be null. Version 1 `--snapshot-dir` is only for genuine legacy sessions, without identity migration or resending.
