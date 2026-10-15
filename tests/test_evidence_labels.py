"""Catch missing evidence destinations and unfinished plain-label migrations."""
from pathlib import Path
import re
import unittest

ROOT = Path(__file__).resolve().parent.parent


class EvidenceLabelTests(unittest.TestCase):
    def test_narrative_labels_have_registered_destinations(self):
        main = (ROOT / 'main.tex').read_text()
        labels = dict(re.findall(r'\\evidencecode\{([^}]+)\}\{([^}]+)\}', main))
        index = (ROOT / 'evidence-2026.tex').read_text()
        anchors = re.findall(r'\\hypertarget\{evidence-([^}]+)\}', index)
        self.assertEqual(len(anchors), len(set(anchors)))
        for name in ('achievements', 'directed', 'nondirected', 'researchandcreative', 'october-updates'):
            text = (ROOT / f'{name}.tex').read_text()
            refs = re.findall(r'\\evidenceref(?:\[([^\]]+)\])?\{([^}]+)\}', text)
            self.assertTrue(refs, name)
            for label, key in refs:
                with self.subTest(section=name, key=key):
                    self.assertIn(key, labels)
                    self.assertIn(key, anchors)
                    self.assertTrue(label, 'Section has an unmigrated coded tag')
                    self.assertNotEqual(label, key)

    def test_chronology_links_have_individual_destinations(self):
        chronology = (ROOT / 'october-updates.tex').read_text()
        sources = '\n'.join((ROOT / f'{name}.tex').read_text()
                            for name in ('directed', 'nondirected', 'researchandcreative'))
        for key in re.findall(r'\\hyperref\[([^]]+)\]', chronology):
            with self.subTest(key=key):
                self.assertEqual(sources.count(r'\phantomsection\label{' + key + '}'), 1)


if __name__ == '__main__':
    unittest.main()
