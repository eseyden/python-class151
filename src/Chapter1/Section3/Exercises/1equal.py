# --------------------------
# Exercise 1.3.1
# (1equal.py)
# Eric/a Seyden
# -------------------------
import sys
import stdio


def main(arg1, arg2, arg3):
    integer1 = int(arg1)
    integer2 = int(arg2)
    integer3 = int(arg3)

    if integer1 == integer2 == integer3:
        stdio.writeln('equal')
    else:
        stdio.writeln('not equal')


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])