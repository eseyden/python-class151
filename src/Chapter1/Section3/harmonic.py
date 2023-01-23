# ------------------------------------------------
# Program 1.3.5 Harmonic numbers
# ( harmonic.py )
# Eric/a Seyden
# 2023-01-21
# ------------------------------------------------

import sys
import stdio


def main(arg1):
    n = int(arg1)

    total = 0.0
    for i in range(1, n+1):
        total += 1.0 / i  # Add the ith term to the sum.

    stdio.writeln(total)


if __name__ == "__main__":
    main(sys.argv[1])
