from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
import Chapter1.Section1.helloworld


class Test(TestCase):
    def test_main(self):
        expected = dedent("""\
            Hello, World
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Chapter1.Section1.helloworld.main()
            self.assertEqual(fake_out.getvalue(), expected)