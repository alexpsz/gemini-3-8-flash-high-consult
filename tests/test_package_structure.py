"""Narrow stdlib checks for this package, not a general YAML validator."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parents[1]


class PackageStructureTests(unittest.TestCase):
    def test_skill_frontmatter_supported_scalar_format(self):
        text = (ROOT / 'SKILL.md').read_text(encoding='utf-8')
        self.assertTrue(text.startswith('---\n'))
        frontmatter, body = text[4:].split('\n---\n', 1)
        fields = {}
        for line in frontmatter.splitlines():
            key, value = line.split(': ', 1)
            self.assertNotIn(key, fields)
            fields[key] = value
        self.assertEqual(set(fields), {'name', 'description', 'license'})
        self.assertEqual(fields['name'], ROOT.name)
        self.assertRegex(fields['name'], r'^[a-z0-9]+(?:-[a-z0-9]+)*$')
        self.assertLessEqual(len(fields['name']), 64)
        self.assertTrue(1 <= len(fields['description']) <= 1024)
        self.assertLess(len(text.splitlines()), 500)
        self.assertTrue(body.strip())

    def test_relative_markdown_links_exist_within_package(self):
        for path in ROOT.rglob('*.md'):
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                if '://' in target or target.startswith('#'):
                    continue
                target = target.split('#', 1)[0]
                resolved = (path.parent / target).resolve()
                self.assertTrue(resolved.is_relative_to(ROOT), (path.name, target))
                self.assertTrue(resolved.is_file(), (path.name, target))

    def test_agent_metadata_is_small_quoted_interface(self):
        text = (ROOT / 'agents' / 'openai.yaml').read_text(encoding='utf-8')
        self.assertTrue(text.startswith('interface:\n'))
        values = {}
        for line in text.splitlines()[1:]:
            match = re.fullmatch(r'  ([a-z_]+): "([^"\n]*)"', line)
            self.assertIsNotNone(match)
            values[match[1]] = match[2]
        self.assertEqual(set(values), {'display_name', 'short_description', 'default_prompt'})
        self.assertTrue(25 <= len(values['short_description']) <= 64)
        self.assertIn('$' + ROOT.name, values['default_prompt'])


if __name__ == '__main__':
    unittest.main()
