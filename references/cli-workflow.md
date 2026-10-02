# Official Antigravity CLI

Use for new consultations. Recover an existing `SENT` or `UNKNOWN` through its original route; changing transport is another submission. A native fallback requires explicit route choice or established `NOT_SENT` and unchanged authorized scope.

## Prepare and dispatch

Check the installed executable/version and `agy models` once per installation, authentication or model-availability change. Use the exact supported slug `gemini-3.8-flash-high` with `--effort high`. Preserve normal harness, skills, rules, plugins and tools; do not add blanket approval flags, suppress skill expansion or replace this route with a direct model API.

## Default web research and profile setup

Relevant public search through `search_web` and page reading through `read_url_content` are part of normal consultation. No separate user request is needed on each run. Honor explicit offline instructions or narrower source limits; having network permission does not require using it for an entirely local question.

For a profile authorized to use default web access, preserve the existing `~/.gemini/antigravity-cli/settings.json` object and append `read_url(*)` once to `permissions.allow`. Preserve other keys and entries, especially explicit `deny` and `ask`; do not replace the file with this illustrative fragment:

```json
{"permissions":{"allow":["read_url(*)"]}}
```

Reuse an existing documented authorization for default web access without asking on each consultation. Check the current user's authorization before changing global settings on a machine or profile; installing the skill alone does not authorize such a change. Back up the affected configuration before an authorized setup, read it back, and recheck only after relevant profile or policy changes.

AGY 1.2.14 has no supported per-run fine-grained allow flag in its help. Keep normal `--mode plan` and the existing configuration; do not add permission hooks or blanket skip flags. The native rule permits domain reading, including browser domain reads and sandbox outbound domains. It does not grant `execute_url`, waive command approval, or add command/file/MCP wildcards. Explicit deny/ask rules and managed policy remain in force. Search has no separately documented `search_web(...)` permission resource; verify actual search and read events rather than inventing a rule or assuming all tools are now unrestricted.

Before a new dispatch, verify the expected rule is present and inspect relevant inherited restrictions. A readable settings file alone does not prove the effective merged policy. Preserve native permission denials and report their effect; stop repeating a rejected action. Do not weaken a rule or resend an existing `SENT`/`UNKNOWN` request to make a network check pass.

## Submit once

Prepare the exact UTF-8 prompt using [packet preparation](context-packet-template.md). Inline bounded evidence when sufficient; otherwise authorize exact file reads. Reuse the approved root and existing project. Do not use `--new-project` merely to consult. Independent advisers may prepare and generate concurrently; one controller owns each request's dispatch.

Predeclare one absolute run directory per request/adviser before its first attempt; inspect existing request records before launch. Run the bundled helper with that unused directory. Confirm its `--help` if the installed helper differs:

```sh
python3 scripts/run_consult.py --adviser gemini --executable /absolute/path/to/agy --project-root /absolute/project --prompt-file /absolute/review/prompt.txt --run-dir /absolute/review/new-run --request-id review-001 --model gemini-3.8-flash-high --effort high --timeout-seconds 300 --sentinel GEMINI38_FLASH_HIGH_RESULT_REVIEW_001
```

Use the verified installed executable path on the current host; the path above is a placeholder. `--sentinel` is optional to the helper but use it when the prompt requires one. Do not reuse a run directory to trigger a second launch, or choose another directory/request ID to bypass a guard for the same request. Recover the recorded attempt; genuinely changed evidence or authorized follow-up gets a separately identified request.

The helper sends one NDJSON stdin message, `{"event":"user","message":{"content":"exact prompt"}}`, closes stdin and collects that turn. It uses `--input-format stream-json --output-format stream-json`, without `-p`. This preserves the prompt outside process arguments. Bare `-p` consumes the next argument; the initial local probe was rejected before submission for this reason. Do not guess that `--print=` or `--print -` accepts text stdin.

## Observe and verify

Keep `run.json`, `answer.md`, `stdout.raw`, `stderr.raw`, `stdin.jsonl` and `native.log`. The receipt records request, parameters, hashes, timing and session IDs; it is separate from the native delivery schema. Confirm `init.cwd` against the approved root before claiming runtime binding. An `init` alone is not submission proof; the helper recognizes native user-input/response/result evidence for `SENT`.

Use receipt fields independently:

- `delivery_status: COMPLETE` means the helper accepted the returned answer and transport checks. Inspect stderr, tool errors, missing reads and timeouts as well; partial text is not completion.
- `target_verification: CONFIGURED` confirms configured model evidence and requested parameters, not effective High. `VERIFIED_NATIVE_METADATA` requires matching native model and effort evidence. Missing effort stays null/unverified; model self-description cannot fill it. `MISMATCH` or `UNKNOWN_UNVERIFIED` must remain visible.
- Preserve the complete original answer before informed follow-up. A correct marker or file fact corroborates that evidence only, not every input or isolation from inherited context.

No external automatic resubmission: after a timeout, lost process output or uncertain dispatch, inspect the saved run first. A new `--conversation` turn sends another message; it is not a read-only recovery command. CLI internal retries need no second controller launch. Soft-denied tools and timeout partial output can accompany exit 0; evaluate each turn's result and limitations. Keep unchanged progress quiet, using bounded process/output observations instead of UI polling.

## Advisory permissions

The consultation prompt makes product files read-only and asks for stdout delivery. This is an instruction, not enforcement: workspace writes may be allowed by existing policy. `--mode plan` adds planning guidance and headless can pass plan review automatically; `--sandbox` is not a read-only filesystem. Do not claim either enforces review-only behavior. The authorized default web rule above is the only profile change described here; do not expand other permissions to make a run succeed. Respect actual denials and verify any separately authorized restrictive policy before relying on it.

Sources: [headless stdin and events](https://www.antigravity.google/docs/cli/headless/), [execution modes](https://www.antigravity.google/docs/cli/modes/), [permissions](https://www.antigravity.google/docs/permissions/), [version changes](https://antigravity.google/docs/changelog?tab=cli). Installed help and actual saved run evidence take precedence over stale examples.

Validation on macOS with `agy 1.2.14` (2026-10-01): the corrected single-message stdin probe returned user-input DONE, successful `view_file`, a complete SUCCESS response and sentinel, exit 0, in 20.608 seconds. Native `init.model` matched the requested slug; native effort was absent. This proves that smoke-test path, not effective effort or every installed customization. It was a direct protocol probe; validate the packaged helper separately.

That probe did not establish search or webpage-read success. Record actual native tool results for the new network configuration before declaring it tested.

`read_url_content` may return a pointer to its saved body instead of inline text. The packet permits the adviser to read that exact tool-generated response in its own conversation, in addition to manifest inputs; do not impose a blanket local-file ban that blocks this research step. A saved response and its wrapper title do not prove the adviser read the page content.

When stream events omit `tool_info.output`, recover evidence read-only from this run's native `conversation_id`: `~/.gemini/antigravity-cli/brain/<conversation_id>/.system_generated/logs/transcript.jsonl` and the exact step output/content files it references. Require the same recorded conversation and step, refuse links or paths escaping that conversation, preserve original bytes with hashes, and distinguish fetched fragments from complete pages. Do not scan other sessions, resend, or ask the model to reconstruct an answer. A DONE event without content remains an observed call rather than proof of source access. This transcript location is documented in [native hook metadata](https://www.antigravity.google/docs/hooks/#common-input-fields); no hook needs to be installed to read it.

The runner exits 0 only for complete delivery with matching configured or verified target metadata. This is not proof of effective effort when that field is absent, nor a factual-review verdict. A native Antigravity print-timeout warning invalidates completion even when the process exits 0 and retains a partial answer.

For default web preflight, reusable setup records, visible login handoff, manifest path checks, live progress, explicit same-conversation follow-up and offline access-evidence collection, follow [runtime checks and recovery](runtime-recovery.md).
