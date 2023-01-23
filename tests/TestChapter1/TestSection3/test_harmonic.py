# ---------------------------------------------
# Test Program 1.3.5 Harmonic numbers
# ( test_harmonic.py )
# Eric(a) Seyden
# 2023-01-23
# ----------------------------------------------

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
from Chapter1.Section3 import harmonic


class Test(TestCase):
    def test_main(self):
        expected = dedent("""\
            1.5
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            harmonic.main(2)
            self.assertEqual(expected, fake_out.getvalue())

        expected = dedent("""\
            2.9289682539682538
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            harmonic.main(10)
            self.assertEqual(expected, fake_out.getvalue())

        expected = dedent("""\
            9.787606036044348
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            harmonic.main(10000)
            self.assertEqual(expected, fake_out.getvalue())
