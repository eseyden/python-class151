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


def main(arg1, arg2, arg3):  # main function, commandline entrypoint

    # cast arguments as float and set to corresponding variable names
    years = float(arg1)
    amount = float(arg2)
    rate = float(arg3)

    total = amount * (math.e ** (rate * years))  # compound interest algorithm

    stdio.writeln(round(total, 2))  # output a rounded total


if __name__ == "__main__":  # checks to see if file is run from command line
    main(sys.argv[1], sys.argv[2], sys.argv[3])  # pass 3 command line arguments to main function
