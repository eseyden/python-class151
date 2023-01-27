# ----------------------------------------------------
# Test Assignment #2
# Exercise 1.2.22 Windchill
# ( test_compound.py )
# Eric(a) Seyden
# 2023-01-20
# -----------------------------------------------------

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
from Assignments import windchill


class Test(TestCase):  # define test class
    def test_main(self):  # test main function
        expected = dedent("""\
            Temperature = 32.0
            Wind speed  = 10.0
            Wind chill  = 23.72714425963738
            """)  # initialize expected output, use dedent, so it aligns with block level
        # patch sys.stdout, so we can capture stdio.writeln()'s output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            windchill.main("32", "10")  # run main function
            self.assertEqual(expected, fake_out.getvalue())  # assert output matches expected output

    def test_main2(self):
        expected = dedent("""\
            Temperature = 10.0
            Wind speed  = 30.0
            Wind chill  = -12.283183932238593
            """)  # initialize expected output, use dedent, so it aligns with block level
        # patch sys.stdout, so we can capture stdio.writeln()'s output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            windchill.main("10", "30")  # run main function
            self.assertEqual(expected, fake_out.getvalue())  # assert output matches expected output
