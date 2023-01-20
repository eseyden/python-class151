from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
from Chapter1.Section2 import leapyear
import calendar
import random


class Test(TestCase):
    def test_2016(self):
        expected = dedent("""\
            True
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            leapyear.main(2016)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_1900(self):
        expected = dedent("""\
            False
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            leapyear.main(1900)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_2000(self):
        expected = dedent("""\
            True
            """)
        with patch('sys.stdout', new=StringIO()) as fake_out:
            leapyear.main(2000)
            self.assertEqual(fake_out.getvalue(), expected)

    def test_random(self):
        for loopCount in range(0, 10000):
            year = random.randint(0, 2100)
            self.assertEqual(leapyear.check_leap(year), calendar.isleap(year))
