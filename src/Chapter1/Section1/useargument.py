# -------------------------------------------
# Program 1.1.2 Using a command-line argument
# ( useargument.py )
# Eric(a) Seyden
# -------------------------------------------

import sys
import stdio


def main(argument1):
    stdio.write('Hi, ')
    stdio.write(argument1)
    stdio.writeln('. How are you?')


if __name__ == '__main__':
    main(sys.argv[1])
