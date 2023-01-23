# ---------------------------------------------
# Test Program 1.3.4 Your first nested loops
# ( test_divisorpattern.py )
# Eric(a) Seyden
# 2023-01-23
# ----------------------------------------------

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
from Chapter1.Section3 import divisorpattern


class Test(TestCase):  # define test class
    def test_main(self):  # test main function
        expected = dedent("""\
            * * * 1
            * *   2
            *   * 3
            """)  # initialize expected output, use dedent, so it aligns with block level
        # patch sys.stdout, so we can capture stdio.writeln()'s output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            divisorpattern.main(3)  # run hello world main function
            self.assertEqual(expected, fake_out.getvalue())  # assert output matches expected output