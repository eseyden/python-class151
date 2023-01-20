from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
import Chapter1.Section2.intops


class Test(TestCase):
    def test_main(self):
        expected = dedent("""\
            1234 +  5 = 1239
            1234 -  5 = 1229
            1234 *  5 = 6170
            1234 // 5 = 246
            1234 %  5 = 4
            1234 ** 5 = 2861381721051424
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            Chapter1.Section2.intops.main(1234, 5)
            self.assertEqual(expected, fake_out.getvalue())
