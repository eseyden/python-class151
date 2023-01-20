# ----------------------------------------------------
# Assignment #1
# Exercise 1.2.21 Continuously compounded interest
# ( compound.py )
# Eric(a) Seyden
# 2023-01-20
# -----------------------------------------------------

import sys
import stdio
import math


def main(arg1, arg2, arg3):
    years = float(arg1)
    amount = float(arg2)
    rate = float(arg3)
    total = amount * (math.e ** (rate * years))
    stdio.writeln(round(total, 2))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
