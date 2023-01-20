# ------------------------------------
# Test Exercise 1.1.1 Hello, World 10
# ( test_helloworld10.py )
# Eric(a) Seyden
# ------------------------------------

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
import Chapter1.Section1.helloworld10


class Test(TestCase):
    def test_main(self):
        expected = dedent("""\
            Hello World!
            Hello World!
            Hello World!
            Hello World!
            Hello World!
            Hello World!
            Hello World!
            Hello World!
            Hello World!
            Hello World!
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Chapter1.Section1.helloworld10.main()
            self.assertEqual(expected, fake_out.getvalue())