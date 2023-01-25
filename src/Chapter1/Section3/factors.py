# ---------------------------------
# Program 1.3.9 Factoring integers
# (factors.py)
# ---------------------------------

import sys
import stdio


def main(arg1):
    n = int(arg1)

    factor = 2
    while factor*factor <= n:
        while (n % factor) == 0:
            n //= factor
            stdio.write(str(factor) + ' ')
        factor += 1

    if n > 1:
        stdio.write(n)
    stdio.writeln()


if __name__ == "__main__":
    main(sys.argv[1])
