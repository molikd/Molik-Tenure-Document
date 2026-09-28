"""Check the real evidence macro's TOC anchor for a non-first-page excerpt."""
import os
from pathlib import Path
import re
import subprocess
import tempfile
import unittest


@unittest.skipUnless(os.environ.get('RUN_LATEX_INTEGRATION') == '1',
                     'requires TeX; opt in with RUN_LATEX_INTEGRATION=1')
class ExcerptAnchorTests(unittest.TestCase):
    def test_excerpt_anchor_lands_on_first_inserted_page(self):
        root = Path(__file__).resolve().parents[1]
        main = (root / 'main.tex').read_text()
        macro = main[main.index(r'\ExplSyntaxOn'):main.index(r'\begin{document}')]
        with tempfile.TemporaryDirectory() as directory:
            work = Path(directory)

            def compile_tex(name):
                result = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', '-halt-on-error', name],
                    cwd=work, capture_output=True, text=True, timeout=90)
                self.assertEqual(result.returncode, 0, result.stdout[-6000:])

            (work / 'source.tex').write_text(
                r'\documentclass{article}\begin{document}'
                r'First\newpage Second\newpage Third\end{document}')
            compile_tex('source.tex')
            (work / 'excerpt.tex').write_text(
                r'\documentclass{article}\usepackage{pdfpages,eso-pic,hyperref}'
                + macro + r'\begin{document}'
                r'\evidencepdf[2,3]{N2.1}{Excerpt}{source.pdf}{3}'
                r'\end{document}')
            compile_tex('excerpt.tex')
            aux = (work / 'excerpt.aux').read_text()
            label = re.search(r'\\newlabel\{supplement-N2\.1\}\{\{[^}]*\}\{(\d+)\}', aux)
            self.assertIsNotNone(label, 'Excerpt must create a TOC destination')
            self.assertEqual(label.group(1), '1', 'Destination must be the first inserted page')


if __name__ == '__main__':
    unittest.main()
