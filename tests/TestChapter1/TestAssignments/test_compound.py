# ----------------------------------------------------
# Test Assignment #1
# Exercise 1.2.21 Continuously compounded interest
# ( test_compound.py )
# Eric(a) Seyden
# 2023-01-20
# -----------------------------------------------------

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
from Assignments import compound


class Test(TestCase):  # define test class
    def test_main(self):  # test main function
        expected = dedent("""\
            1624.93
            """)  # initialize expected output, use dedent, so it aligns with block level
        # patch sys.stdout, so we can capture stdio.writeln()'s output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            compound.main("2", "1500", ".04")  # run main function
            self.assertEqual(expected, fake_out.getvalue())  # assert output matches expected output

    def test_main2(self):
        expected = dedent("""\
            2237.74
            """)  # initialize expected output, use dedent, so it aligns with block level
        # patch sys.stdout, so we can capture stdio.writeln()'s output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            compound.main("10", "1500", ".04")  # run main function
            self.assertEqual(expected, fake_out.getvalue())  # assert output matches expected output
