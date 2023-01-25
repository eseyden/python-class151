# ------------------------------------------------
# Exercise 1.3.3 Quadratic formula
# ( 2floatrange.py )
# Eric/a Seyden
# 2023-01-24
# ------------------------------------------------

import sys
import stdio


def main(arg1, arg2):
    float_x = float(arg1)
    float_y = float(arg2)
    if 1.0 > float_x > 0.0 and 1.0 > float_y > 0.0:
        stdio.writeln('True')
    else:
        stdio.writeln('False')


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
