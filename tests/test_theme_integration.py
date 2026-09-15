"""Compile theme selection without any color command defined before the class."""
import os
from pathlib import Path
import shutil
import subprocess
import tempfile
import unittest


@unittest.skipUnless(os.environ.get('RUN_LATEX_INTEGRATION') == '1',
                     'requires TeX; opt in with RUN_LATEX_INTEGRATION=1')
class ThemeLoadingTests(unittest.TestCase):
    def test_shared_preamble_accepts_literal_root_colors(self):
        root = Path(__file__).resolve().parents[1]
        for color in ('purple', 'black'):
            with self.subTest(color=color), tempfile.TemporaryDirectory() as directory:
                copy = Path(directory) / 'repo'
                shutil.copytree(root, copy, ignore=shutil.ignore_patterns(
                    '.git', 'build', '__pycache__'))
                source = copy / 'theme-smoke.tex'
                source.write_text(
                    '\\input{shared/preamble}\n'
                    f'\\moderncvcolor{{{color}}}\n'
                    '\\makeatletter\n'
                    f'\\@ifpackageloaded{{moderncvcolor{color}}}{{}}{{'
                    '\\errmessage{Expected theme was not loaded}}\n'
                    '\\makeatother\n'
                    '\\firstname{Theme}\\familyname{Test}\n'
                    '\\begin{document}\n'
                    '\\textcolor{color1}{Theme loading regression}\n'
                    '\\end{document}\n')
                result = subprocess.run(
                    ['pdflatex', '-interaction=nonstopmode', '-halt-on-error',
                     source.name], cwd=copy, capture_output=True, text=True,
                    timeout=90)
                self.assertEqual(result.returncode, 0, result.stdout[-6000:])
                self.assertTrue((copy / 'theme-smoke.pdf').is_file())


if __name__ == '__main__':
    unittest.main()
