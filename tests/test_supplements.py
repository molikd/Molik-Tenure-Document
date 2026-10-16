"""Keep original evidence intact and verify full/excerpt/omitted selections."""
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent.parent


class SupplementTests(unittest.TestCase):
    def test_manifest_matches_pdf_selections(self):
        records = json.loads((ROOT / 'evidence/supplements.json').read_text())
        source = '\n'.join((ROOT / name).read_text() for name in (
            'supplements-2026.tex', 'directed-evidence-2026.tex',
            'nondirected-evidence-2026.tex', 'research-evidence-2026.tex',
            'evaluations-2026.tex', 'reappointment-letters.tex'))
        includes = re.findall(
            r'\\evidencepdf(?:\[([^\]]+)\])?\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}\{(\d+)\}', source)
        expected = []
        index = (ROOT / 'evidence-2026.tex').read_text()
        for record in records:
            with self.subTest(mark=record['mark']):
                content = (ROOT / record['path']).read_bytes()
                self.assertTrue(content.startswith(b'%PDF-'))
                self.assertEqual(hashlib.sha256(content).hexdigest(), record['sha256'])
                pages = record.get('included_pages')
                if pages is not None:
                    self.assertEqual(pages, sorted(set(pages)))
                    self.assertTrue(all(isinstance(p, int) and 1 <= p <= record['pages'] for p in pages))
                    self.assertTrue(record['note'])
                if pages == []:
                    self.assertNotIn('supplement-' + record['mark'] + ']', index)
                    self.assertIn(record['path'], index)
                    continue
                assembly_path = record.get('assembly_path', record['path'])
                if 'assembly_path' in record:
                    self.assertEqual(hashlib.sha256((ROOT / assembly_path).read_bytes()).hexdigest(), record['assembly_sha256'])
                selection = '' if pages is None else ','.join(map(str, pages))
                expected.append((selection, record['mark'], record['title'], assembly_path, str(record['pages'])))
                self.assertIn('supplement-' + record['mark'] + ']', index)
                self.assertIn('evidence-' + record['mark'].split('.')[0] + '}', index)
        self.assertCountEqual(includes, expected)
        self.assertEqual(len({r['mark'] for r in records}), len(records))
        self.assertEqual(len({r['path'] for r in records}), len(records))
        self.assertEqual(re.findall(r'\\hyperref\[supplement-([^]]+)\]', source),
                         [r['mark'] for r in records if r.get('included_pages') != []])

    def test_packet_follows_supplied_document_order(self):
        main = (ROOT / 'main.tex').read_text()
        names = ('recommendation-form', 'achievements', 'goals', 'directed',
                 'directed-evidence-2026', 'nondirected', 'nondirected-evidence-2026',
                 'researchandcreative', 'research-evidence-2026', 'evaluations-2026',
                 'reappointment-letters', 'cv', 'october-updates', 'evidence-2026',
                 'supplements-2026')
        positions = [main.index(r'\input{' + name + '.tex}') for name in names]
        self.assertEqual(positions, sorted(positions))
        self.assertLess(positions[0], main.index('Employment History'))
        self.assertLess(main.index('Employment History'), positions[1])
        letter = (ROOT / 'reappointment-letters.tex').read_text()
        self.assertIn('evidence/2025/reappointment-letter-signed.pdf', letter)


if __name__ == '__main__':
    unittest.main()
