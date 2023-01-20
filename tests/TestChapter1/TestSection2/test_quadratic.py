from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
import Chapter1.Section2.quadratic


class Test(TestCase):
    def test_main(self):
        expected = dedent("""\
            2.0
            1.0
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Chapter1.Section2.quadratic.main(-3.0, 2.0)
            self.assertEqual(expected, fake_out.getvalue())

    def test_main_float(self):
        expected = dedent("""\
            1.618033988749895
            -0.6180339887498949
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Chapter1.Section2.quadratic.main(-1.0, -1.0)
            self.assertEqual(expected, fake_out.getvalue())

    def test_main_error(self):
        with self.assertRaises(ValueError):  # check that invalid input raises a Value Error
            Chapter1.Section2.quadratic.main(1.0, 1.0)
