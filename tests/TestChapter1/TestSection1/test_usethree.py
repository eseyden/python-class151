from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
import Chapter1.Section1.usethree


class Test(TestCase):
    def test_main(self):
        expected = dedent("""\
            Hi, Hal, Frank, and Dave
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Chapter1.Section1.usethree.main('Dave', 'Frank', 'Hal')
            self.assertEqual(expected, fake_out.getvalue())
