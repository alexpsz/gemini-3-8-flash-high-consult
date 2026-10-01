# Gemini 3.8 Flash High Consult

A standalone Agent Skill for independent reviews in Antigravity desktop. It verifies the selected model, limits evidence to named files, submits once, and preserves the complete original answer in the owning project. It does not include an account, API key, native automation runtime or personal consultation history.

## Install

Copy this repository directory as `gemini-3-8-flash-high-consult` into your agent's configured skills directory. For a Codex installation using the conventional default, that is `~/.codex/skills/` on macOS or `$HOME\.codex\skills\` in Windows PowerShell. Respect an existing skill rather than overwriting it blindly. If your installed client uses another discovery location, use its current documented location.

Invoke: `Use $gemini-3-8-flash-high-consult to review this artifact in its owning project.`

Antigravity must be installed, signed in and expose the requested model in its actual picker. A supported native computer-use capability is also required. This skill discovers and follows that capability's current documentation. It does not claim a Windows runtime works on macOS. Native macOS interaction remains unverified; the offline protocol is portable Python. Antigravity's [official setup documentation](https://www.antigravity.google/docs) describes current application platform support, which is separate from automation support and model availability.

## Local validation

Python 3.10+ is enough; there are no third-party script dependencies.

```sh
python3 -m unittest discover -s tests -v
python3 scripts/check_packet_safety.py SKILL.md README.md references/context-packet-template.md
```

On Windows substitute your available Python command. Tests use temporary synthetic data and do not contact a model. See [publication checks](PUBLICATION_CHECK.md) for tested scope and limitations. See [SKILL.md](SKILL.md) for the operating workflow and linked protocol references.

The structure follows the [Agent Skills specification](https://agentskills.io/specification); `agents/openai.yaml` is optional Codex UI metadata. This is an independent community package, not an official Google or OpenAI product. Model access and interface labels may change; the workflow stops accurately when the requested target cannot be verified.

MIT license. No upstream license or attribution notice existed in the local source package inspected for this release; the release adds the repository's MIT grant. All examples and tests are synthetic. No provider SDK, application binary or third-party manual is bundled.
