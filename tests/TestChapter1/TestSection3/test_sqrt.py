# ---------------------------------------------
# Test Program 1.3.6 Newton's method
# ( test_sqrt.py )
# Eric(a) Seyden
# 2023-01-23
# ----------------------------------------------

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
from Chapter1.Section3 import sqrt

class Test(TestCase):
    def test_main(self):
        expected = dedent("""\
            1.414213562373095
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            sqrt.main(2)
            self.assertEqual(expected, fake_out.getvalue())

        expected = dedent("""\
            1595.1630010754388
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            sqrt.main(2544545)
            self.assertEqual(expected, fake_out.getvalue())
