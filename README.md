# Gemini 3.8 Flash High Consult

Independent Antigravity reviews through a connected official browser client or CLI, with bounded evidence, single submission and preserved original delivery. Requires a signed-in official client and access to Gemini 3.8 Flash High; CLI helpers require Python 3.10+. Normal harness customization remains enabled; native desktop remains available when selected.

Relevant public search and webpage reading are default consultation capabilities, subject to explicit offline instructions and existing policy. [CLI workflow](references/cli-workflow.md) describes the user-authorized `read_url(*)` profile setup without blanket approval or removing tools. Installing on another machine does not itself authorize global configuration changes. Actual network success must be established from each run's native tool evidence; earlier file-reading probes did not test this configuration.

Install this folder as `gemini-3-8-flash-high-consult` in the configured skills directory, preserving an existing installation. Invoke: `Use $gemini-3-8-flash-high-consult to review this artifact in its owning project.` Start with [SKILL.md](SKILL.md); read supporting references when their phase applies.

For interactive consultations, prefer [browser workflow](references/browser-workflow.md) in the official client connected to the intended machine/project. Use [CLI workflow](references/cli-workflow.md) for background automation, exact parameters or automatic raw-output capture. Retain each run's actual validation evidence. Mac manual-assisted native submission and delivery have been observed; automatic desktop selection/input/send remain unverified. CLI completion does not prove effective effort when native metadata omits it.

Both browser and CLI can write authorized local records. Preserve original answers and actual tool activity separately from model-written summaries; verify named output files on the intended machine. Account or machine sharing alone does not establish complete skill/plugin parity.

Run local checks in a writable copy; they contact no model:

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_packet_safety.py SKILL.md README.md references/context-packet-template.md
```

No provider SDK or automation runtime is bundled. This community package uses the MIT license and is not an official Google or OpenAI product.

For native Windows installation, profile creation and a first live test, follow [Windows CLI setup](references/windows-setup.md). Fixed runtime profiles are generated locally and must not be committed. On Windows use `py -3` in place of `python3` in the offline commands above.
