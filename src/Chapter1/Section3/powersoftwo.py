# ------------------------------------------------
# Program 1.3.3 Computing powers of 2
# ( powersoftwo.py )
# Eric/a Seyden
# 2023-01-23
# ------------------------------------------------

import sys
import stdio


def main(arg1):
    n = int(arg1)  # cast main argument as integer
    power = 1  # init power accumulator
    i = 0  # init loop counter
    while i <= n:  # run loop until counter more than main argument
        stdio.writeln(str(i) + ' ' + str(power))
        power = 2 * power
        i = i + 1


if __name__ == "__main__":
    main(sys.argv[1])
