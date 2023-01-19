# ------------------------------------------------
# Exercise 1.1.6 Using three command-line arguments
# ( usethree.py )
# Eric(a) Seyden
# 2023-01-18
# ------------------------------------------------

import sys  # import library for reading command line arguments
import stdio  # import textbook IO library


def main(name1, name2, name3):  # main function
    # prints Hi and three parameters to standard output
    stdio.write('Hi, ')
    stdio.write(name1)
    stdio.write(', ')
    stdio.write(name2)
    stdio.write(', and ')
    stdio.writeln(name3)


if __name__ == '__main__':  # command line call check
    # __name__ will be set to __main__
    # if library is the entrypoint when being called
    # from command line
    main(sys.argv[1], sys.argv[2], sys.argv[3])  # call main with 3 command line arguments
