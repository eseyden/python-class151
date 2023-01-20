# ---------------------------------
# Test Program 1.1.1 Hello, World
# ( test_helloworld.py )
# Eric(a) Seyden
# 2023-01-20
# ----------------------------------

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
import Chapter1.Section1.helloworld


class Test(TestCase):  # define test class
    def test_main(self):  # test main function
        expected = dedent("""\
            Hello, World
            """)  # initialize expected output, use dedent, so it aligns with block level
        # patch sys.stdout, so we can capture stdio.writeln()'s output
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Chapter1.Section1.helloworld.main()  # run hello world main function
            self.assertEqual(expected, fake_out.getvalue())  # assert output matches expected output
