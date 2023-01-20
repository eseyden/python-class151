from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
import Chapter1.Section2.floatops


class Test(TestCase):
    def test_main(self):
        expected = dedent("""\
            123.456 +  78.9 = 202.356
            123.456 -  78.9 = 44.556
            123.456 *  78.9 = 9740.6784
            123.456 /  78.9 = 1.5647148288973383
            123.456 ** 78.9 = 1.0478827916671325e+165
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Chapter1.Section2.floatops.main(123.456, 78.9)
            self.assertEqual(expected, fake_out.getvalue())
