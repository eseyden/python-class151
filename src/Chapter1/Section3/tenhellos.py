# ------------------------------------------------
# Program 1.3.2 Your first loop
# ( tenhellos.py )
# Eric/a Seyden
# 2023-01-21
# ------------------------------------------------

import stdio


def main():

    stdio.writeln('1st Hello')
    stdio.writeln('2nd Hello')
    stdio.writeln('3rd Hello')

    i = 4
    while i <= 10:
        stdio.writeln(str(i) + "th Hello")
        i = i + 1


if __name__ == "__main__":
    main()
