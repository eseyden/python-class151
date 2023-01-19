from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
import Chapter1.Section2.ruler


class Test(TestCase):
    def test_main(self):
        expected = dedent("""\
            1
            1 2 1
            1 2 1 3 1 2 1
            1 2 1 3 1 2 1 4 1 2 1 3 1 2 1
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Chapter1.Section2.ruler.main()
            self.assertEqual(fake_out.getvalue(), expected)
