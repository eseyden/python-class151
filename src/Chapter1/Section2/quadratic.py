# ------------------------------------------------
# Program 1.2.4 Quadratic formula
# ( quadratic.py )
# Eric/a Seyden
# 2023-01-19
# ------------------------------------------------

import math
import sys
import stdio


def main(arg1, arg2):
    b = float(arg1)
    c = float(arg2)

    discriminant = b*b - 4.0*c
    d = math.sqrt(discriminant)

    stdio.writeln((-b + d) / 2.0)
    stdio.writeln((-b - d) / 2.0)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])