# ----------------------------------------------------
# Test Assignment #1
# Exercise 1.2.21 Continuously compounded interest
# ( test_compound.py )
# Eric(a) Seyden
# 2023-01-20
# -----------------------------------------------------

from io import StringIO
from textwrap import dedent
from unittest import TestCase
from unittest.mock import patch
from Assignments import boysandgirls

sudo_random_values = [1, 1, 0]
sudo_random_values2 = [1, 1, 1, 1, 0]


def my_randint(start, end):
    return sudo_random_values.pop(0)


def my_randint2(start, end):
    global sudo_random_values2
    if len(sudo_random_values2) == 0:
        sudo_random_values2 = [0, 0, 1]
    return sudo_random_values2.pop(0)


class Test(TestCase):
    def test_run_trial(self):
        with patch('random.randint', my_randint):
            result = boysandgirls.run_trial()  # run main function
            self.assertEqual(3, result)  # assert output matches expected output

    def test_run_main(self):
        expected = dedent("""\
            Avg # children: 3
            Trials with 2 children: 0
            Trials with 3 children: 9
            Trials with 4 children: 0
            Trials with 5 or more children: 1
            """)
        with patch('random.randint', my_randint2):
            with patch('sys.stdout', new=StringIO()) as fake_out:
                result = boysandgirls.main(10)  # run main function
                self.assertEqual(expected, fake_out.getvalue())  # assert output matches expected output

