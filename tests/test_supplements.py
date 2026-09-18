"""Keep source evidence intact and every manifest item in the final appendix."""
import hashlib
import json
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent.parent


class SupplementTests(unittest.TestCase):
    def test_manifest_matches_complete_pdf_inclusions(self):
        records = json.loads((ROOT / 'evidence/supplements.json').read_text())
        source = (ROOT / 'supplements-2026.tex').read_text()
        includes = re.findall(r'\\evidencepdf\{([^}]+)\}\{([^}]+)\}\{([^}]+)\}\{(\d+)\}', source)
        self.assertEqual(includes, [(r['mark'], r['title'], r['path'], str(r['pages'])) for r in records])
        self.assertEqual(len({r['mark'] for r in records}), len(records))
        self.assertEqual(len({r['path'] for r in records}), len(records))
        index = (ROOT / 'evidence-2026.tex').read_text()
        for record in records:
            with self.subTest(mark=record['mark']):
                content = (ROOT / record['path']).read_bytes()
                self.assertTrue(content.startswith(b'%PDF-'))
                self.assertEqual(hashlib.sha256(content).hexdigest(), record['sha256'])
                self.assertIn('supplement-' + record['mark'] + ']', index)
                self.assertIn('evidence-' + record['mark'].split('.')[0] + '}', index)

    def test_supplements_follow_cv_and_source_index(self):
        main = (ROOT / 'main.tex').read_text()
        self.assertLess(main.index(r'\input{cv.tex}'), main.index(r'\input{evidence-2026.tex}'))
        self.assertLess(main.index(r'\input{evidence-2026.tex}'), main.index(r'\input{supplements-2026.tex}'))
        self.assertRegex(main, r'\\input\{supplements-2026.tex\}\s*\\end\{document\}')
        self.assertIn(r'\includepdf[pages=-', main)


if __name__ == '__main__':
    unittest.main()
