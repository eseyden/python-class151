# ------------------------------------------
# Test Exercise 1.3.1 Flipping a fair coin
# ( test_flip.py )
# Eric(a) Seyden
# 2023-01-22
# ------------------------------------------

from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
from Chapter1.Section3 import flip


class Test(TestCase):
    def test_main(self):
        heads_output = dedent("""\
            Heads
            """)
        tails_output = dedent("""\
            Tails
            """)
        heads_count = 0
        tails_count = 0
        total_flips = 150
        for count in range(0, total_flips):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                flip.main()
                value = fake_out.getvalue()
            if value == heads_output:
                heads_count += 1
            if value == tails_output:
                tails_count += 1
        heads_percentage = heads_count / total_flips
        tails_percentage = tails_count / total_flips

        self.assertLess(heads_percentage, 0.6)
        self.assertGreater(heads_percentage, 0.4)
        self.assertLess(tails_percentage, 0.6)
        self.assertGreater(tails_percentage, 0.4)