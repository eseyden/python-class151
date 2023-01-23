# ---------------------------------
# Test Program 1.3.2 Your first loop
# ( test_tenhellos.py )
# Eric(a) Seyden
# 2023-01-22
# ----------------------------------

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
from Chapter1.Section3 import tenhellos


class Test(TestCase):  # define test class
    def test_main(self):  # test main function
        expected = dedent("""\
            1st Hello
            2nd Hello
            3rd Hello
            4th Hello
            5th Hello
            6th Hello
            7th Hello
            8th Hello
            9th Hello
            10th Hello
            """)  # initialize expected output, use dedent, so it aligns with block level
        # patch sys.stdout, so we can capture stdio.writeln()'s output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            tenhellos.main()  # run hello world main function
            self.assertEqual(expected, fake_out.getvalue())  # assert output matches expected output
