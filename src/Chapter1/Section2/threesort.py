# ------------------------------------------------
# Exercise 1.2.31 Three-sort
# ( threesort.py )
# Eric/a Seyden
# 2023-01-20
# ------------------------------------------------

import sys
import stdio


def main(arg1, arg2, arg3):
    number1 = int(arg1)
    number2 = int(arg2)
    number3 = int(arg3)

    stdio.writeln(min(number1, number2, number3))
    stdio.writeln(max(min(number1, number2), min(number2, number3), min(number1, number3)))
    stdio.writeln(max(number1, number2, number3))


if __name__ == "__main__":
    if len(sys.argv) == 4:
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        stdio.writeln("Please provide 3 number arguments.")
