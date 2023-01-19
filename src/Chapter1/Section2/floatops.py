# ------------------------------------------------
# Program 1.2.3 Integer Operators
# ( intops.py )
# Eric/a Seyden
# 2023-01-18
# ------------------------------------------------

import stdio
import sys


def main(arg1, arg2):
    a = float(arg1)
    b = float(arg2)

    total = a + b
    diff = a - b
    prod = a * b
    quot = a / b
    exp = a ** b

    stdio.writeln(str(a) + ' + ' + str(b) + ' = ' + str(total))
    stdio.writeln(str(a) + ' - ' + str(b) + ' = ' + str(diff))
    stdio.writeln(str(a) + ' * ' + str(b) + ' = ' + str(prod))
    stdio.writeln(str(a) + ' / ' + str(b) + ' = ' + str(quot))
    stdio.writeln(str(a) + ' ** ' + str(b) + ' = ' + str(exp))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
