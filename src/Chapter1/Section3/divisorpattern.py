# ------------------------------------------------
# Program 1.3.4 Your first nested loops
# ( divisorpattern.py )
# Eric/a Seyden
# 2023-01-23
# ------------------------------------------------

import sys
import stdio


def main(arg1):
    n = int(arg1)
    for i in range(1, n+1):
        # Write the ith line.
        for j in range(1, n+1):
            # Write the jth entry in the ith line.
            if (i % j == 0) or (j % i == 0):
                stdio.write('* ')
            else:
                stdio.write('  ')
        stdio.writeln(i)


if __name__ == "__main__":
    main(sys.argv[1])
