from io import StringIO
from unittest import TestCase
from unittest.mock import patch
from copy import deepcopy
from random import randint
from Chapter1.Section2 import threesort


class Test(TestCase):
    def test_main(self):
        numbers = [randint(0, 10000), randint(0, 10000), randint(0, 1000)]
        sorted_numbers = deepcopy(numbers)
        sorted_numbers.sort()
        expected = ""
        for number in sorted_numbers:
            expected += str(number) + "\n"
        with patch('sys.stdout', new=StringIO()) as fake_out:
            threesort.main(*numbers)
            self.assertEqual(expected, fake_out.getvalue())
