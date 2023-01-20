from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from textwrap import dedent
from Chapter1.Section2 import stats

sudo_random_values = [0.1, 0.2, 0.3, 0.4, 0.5]

test_case = None  # type: Test


class Test(TestCase):
    def test_main(self):
        global test_case
        test_case = self
        expected = dedent("""\
            Number 1 : 0.1
            Number 2 : 0.2
            Number 3 : 0.3
            Number 4 : 0.4
            Number 5 : 0.5
            Average  : 0.3
            Minimum  : 0.1
            Maximum  : 0.5
            """)
        with patch('random.uniform', my_uniform):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                stats.main()
                self.assertEqual(expected, fake_out.getvalue())


def my_uniform(min_value, max_value):
    test_case.assertEqual(0.0, min_value)
    test_case.assertEqual(0.1, max_value)
    return sudo_random_values.pop(0)
