# ------------------------------------------------
# Program 1.1.2 Using three command-line arguments
# ( usethree.py )
# Eric(a) Seyden
# 2023-01-18
# ------------------------------------------------

import sys
import stdio


def main():
    stdio.write('Hi, ')
    stdio.write(sys.argv[1])
    stdio.write(', ')
    stdio.write(sys.argv[2])
    stdio.write(', and ')
    stdio.writeln(sys.argv[3])


if __name__ == '__main__':
    main()
