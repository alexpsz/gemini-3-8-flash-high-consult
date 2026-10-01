"""Shared-directory delivery tests, independent of live model capability."""
import hashlib
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
import collect_delivery as c


class NamedDeliveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.session_path = self.root / 'r1.gemini.session.json'
        self.receipt = self.root / 'r1.gemini.receipt.json'
        self.session = {
            'schema_version': 2, 'request_id': 'r1', 'adviser': 'gemini',
            'input_manifest_sha256': 'a' * 64, 'output_directory': str(self.root),
            'report_file': 'r1.gemini.report.md', 'completion_file': 'r1.gemini.completion.json',
            'findings_file': None, 'sentinel': 'END-R1', 'dispatch_state': 'SENT',
            'generation_stopped': True, 'unresolved_approval': False,
        }
        self.completion = {
            'schema_version': 2, 'request_id': 'r1', 'adviser': 'gemini',
            'input_manifest_sha256': 'a' * 64, 'status': 'complete',
            'report_file': 'r1.gemini.report.md', 'findings_file': None,
        }
        self.report = b'# r1\nIndependent recommendation.\nEND-R1\n'
        (self.root / self.session['report_file']).write_bytes(self.report)
        self.write(self.root / self.session['completion_file'], self.completion)
        self.write(self.session_path, self.session)

    def write(self, path, value):
        path.write_text(json.dumps(value), encoding='utf-8')

    def collect(self):
        return c.collect(self.session_path, stable_seconds=0, receipt_file=self.receipt)

    def failure(self, code):
        with self.assertRaises(c.DeliveryError) as caught:
            self.collect()
        self.assertEqual(caught.exception.code, code)

    def test_shared_directory_only_reads_selected_files(self):
        (self.root / 'other.opus.report.md').write_bytes(b'OTHER PRIVATE REVIEW')
        (self.root / 'packet.md').write_bytes(b'neutral material')
        (self.root / 'subdirectory').mkdir()
        with mock.patch.object(c, 'read_file', wraps=c.read_file) as reads:
            self.assertEqual(self.collect()['file_count'], 2)
        self.assertNotIn('other.opus.report.md', [call.args[0].name for call in reads.call_args_list])
        receipt = json.loads(self.receipt.read_bytes())
        self.assertEqual(receipt['files']['r1.gemini.report.md']['sha256'], hashlib.sha256(self.report).hexdigest())

    def test_identical_retry_does_not_rewrite_receipt(self):
        self.collect()
        original = (self.receipt.read_bytes(), self.receipt.stat().st_mtime_ns)
        self.assertEqual(self.collect()['receipt_action'], 'RECOVERED_IDENTICAL')
        self.assertEqual(original, (self.receipt.read_bytes(), self.receipt.stat().st_mtime_ns))

    def test_missing_completion_and_wrong_identity_are_incomplete(self):
        path = self.root / self.session['completion_file']
        path.unlink()
        self.failure('MISSING_DELIVERABLE')
        self.write(path, {**self.completion, 'adviser': 'opus'})
        self.failure('IDENTITY_MISMATCH')

    def test_named_path_and_controller_overlap_rejected(self):
        for name in ('../other.md', 'c:/other.md', 'report.md:ads', 'sub/report.md', 'CON.md'):
            self.write(self.session_path, {**self.session, 'report_file': name})
            self.failure('INVALID_DELIVERABLE_NAME')
        self.write(self.session_path, {**self.session, 'report_file': self.session_path.name})
        self.failure('CONTROLLER_PATH_OVERLAP')

    def test_source_mutation_rejected_but_other_writer_is_allowed(self):
        with mock.patch.object(c.time, 'sleep', side_effect=lambda _: (self.root / 'other.report.md').write_bytes(b'new')):
            self.assertEqual(self.collect()['status'], 'PASS')
        with mock.patch.object(c.time, 'sleep', side_effect=lambda _: (self.root / self.session['report_file']).write_bytes(self.report.replace(b'Independent', b'Revised'))):
            self.failure('DELIVERY_CHANGED_DURING_STABILITY')

    def test_changed_report_after_receipt_is_rejected(self):
        self.collect()
        (self.root / self.session['report_file']).write_bytes(self.report.replace(b'Independent', b'Changed'))
        self.failure('RECEIPT_CONFLICT')

    def test_missing_sentinel_and_running_ui_state_rejected(self):
        (self.root / self.session['report_file']).write_bytes(self.report + b'continued')
        self.failure('REPORT_SENTINEL_MISSING')
        self.write(self.session_path, {**self.session, 'generation_stopped': False})
        self.failure('GENERATION_NOT_STOPPED')

    def test_optional_findings_and_required_findings(self):
        self.write(self.session_path, {**self.session, 'findings_file': 'r1.gemini.findings.json', 'findings_required': True})
        self.failure('REQUIRED_FINDINGS_MISSING')
        self.write(self.root / self.session['completion_file'], {**self.completion, 'findings_file': 'r1.gemini.findings.json'})
        self.write(self.root / 'r1.gemini.findings.json', {
            'schema_version': 2, 'request_id': 'r1', 'adviser': 'gemini',
            'input_manifest_sha256': 'a'*64, 'recommendation': 'Keep current design.',
            'findings': [], 'evidence_read': ['packet.md'], 'unknowns': [],
        })
        self.assertEqual(self.collect()['file_count'], 3)

    def test_case_variant_controller_alias_is_refused_on_every_host(self):
        self.write(self.session_path, {**self.session, 'report_file': self.session_path.name.upper()})
        self.failure('CONTROLLER_PATH_OVERLAP')

    def test_case_variant_receipt_cannot_alias_report(self):
        self.receipt = self.root / self.session['report_file'].upper()
        self.failure('CONTROLLER_PATH_OVERLAP')

    def test_symlink_receipt_cannot_read_or_overwrite_another_file(self):
        target = self.root / 'unrelated.txt'
        target.write_bytes(b'preserve unrelated content')
        try:
            self.receipt.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest('Host does not permit symlink creation')
        self.failure('LINK_OR_REPARSE_REFUSED')
        self.assertEqual(target.read_bytes(), b'preserve unrelated content')

    def test_named_report_symlink_is_refused(self):
        report = self.root / self.session['report_file']
        report.unlink()
        target = self.root / 'unrelated-report.txt'
        target.write_bytes(self.report)
        try:
            report.symlink_to(target)
        except (OSError, NotImplementedError):
            self.skipTest('Host does not permit symlink creation')
        self.failure('LINK_OR_REPARSE_REFUSED')


if __name__ == '__main__':
    unittest.main()
