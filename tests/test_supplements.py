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
        source = (ROOT / 'supplements-2026.tex').read_text()
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
                selection = '' if pages is None else ','.join(map(str, pages))
                expected.append((selection, record['mark'], record['title'], record['path'], str(record['pages'])))
                self.assertIn('supplement-' + record['mark'] + ']', index)
                self.assertIn('evidence-' + record['mark'].split('.')[0] + '}', index)
        self.assertEqual(includes, expected)
        self.assertEqual(len({r['mark'] for r in records}), len(records))
        self.assertEqual(len({r['path'] for r in records}), len(records))
        self.assertEqual(re.findall(r'\\hyperref\[supplement-([^]]+)\]', source),
                         [r['mark'] for r in records if r.get('included_pages') != []])

    def test_supplements_follow_cv_and_source_index(self):
        main = (ROOT / 'main.tex').read_text()
        self.assertLess(main.index(r'\input{cv.tex}'), main.index(r'\input{evidence-2026.tex}'))
        self.assertLess(main.index(r'\input{evidence-2026.tex}'), main.index(r'\input{supplements-2026.tex}'))
        self.assertRegex(main, r'\\input\{supplements-2026.tex\}\s*\\end\{document\}')


if __name__ == '__main__':
    unittest.main()
