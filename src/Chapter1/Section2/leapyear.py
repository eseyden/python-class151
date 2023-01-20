# ------------------------------------------------
# Program 1.2.5 Leap year
# ( leapyear.py )
# Eric/a Seyden
# 2023-01-19
# ------------------------------------------------
import sys
import stdio


def main(arg1):
    stdio.writeln(check_leap(arg1))


def check_leap(year):
    year = int(year)
    isLeapYear = (year % 4 == 0)
    isLeapYear = isLeapYear and ((year % 100) != 0)
    isLeapYear = isLeapYear or ((year % 400) == 0)
    return isLeapYear


if __name__ == "__main__":
    main(sys.argv[1])
