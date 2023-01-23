# ---------------------------------------------
# Program 1.3.6 Newton's method (sqrt.py)
# ( sqrt.py )
# Eric(a) Seyden
# 2023-01-23
# ----------------------------------------------

import sys
import stdio

EPSILON = 1e-15


def main(arg1):
    c = float(arg1)
    t = c
    while abs(t - c/t) > (EPSILON * t):
        t = (c/t + t) / 2.0
    stdio.writeln(t)


if __name__ == "__main__":
    main(sys.argv[1])
