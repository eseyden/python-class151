# ---------------------------------------------
# Test Program 1.3.3 Computing powers of 2
# ( test_powersoftwo.py )
# Eric(a) Seyden
# 2023-01-23
# ----------------------------------------------

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
from Chapter1.Section3 import powersoftwo


class Test(TestCase):  # define test class
    def test_main(self):  # test main function
        expected = dedent("""\
            0 1
            1 2
            2 4
            3 8
            4 16
            5 32
            """)  # initialize expected output, use dedent, so it aligns with block level
        # patch sys.stdout, so we can capture stdio.writeln()'s output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            powersoftwo.main(5)  # run hello world main function
            self.assertEqual(expected, fake_out.getvalue())  # assert output matches expected output