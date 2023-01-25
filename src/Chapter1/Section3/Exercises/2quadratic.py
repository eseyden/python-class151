# ------------------------------------------------
# Exercise 1.3.2 Quadratic formula
# ( 1quadratic.py )
# Eric/a Seyden
# 2023-01-24
# ------------------------------------------------

import math
import sys
import stdio


def main(arg1, arg2, arg3):
    a = float(arg1)
    b = float(arg2)
    c = float(arg3)

    if a == 0:
        stdio.writeln('a cannot be zero')
        return

    discriminant = b*b - 4.0*a*c

    if discriminant < 0:
        stdio.writeln('discriminant less than zero')
        return

    d = math.sqrt(discriminant)

    divisor = (2.0 * a)
    stdio.writeln((-b + d) / divisor)
    stdio.writeln((-b - d) / divisor)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2], sys.argv[3])
