# -------------------------------------------
# Test Program 1.1.2 Using a command-line argument
# ( test_useargument.py )
# Eric(a) Seyden
# 2023-01-20
# -------------------------------------------
from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
import Chapter1.Section1.useargument


class Test(TestCase):
    def test_main(self):
        expected = dedent("""\
            Hi, Dave. How are you?
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Chapter1.Section1.useargument.main('Dave')
            self.assertEqual(expected, fake_out.getvalue())
