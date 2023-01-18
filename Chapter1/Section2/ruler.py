# ------------------------------------------------
# Program 1.2.1 String concatenation example
# ( ruler.py )
# Eric/a Seyden
# 2023-01-18
# ------------------------------------------------

import stdio


def main():
    ruler1 = '1'
    ruler2 = ruler1 + ' 2 ' + ruler1
    ruler3 = ruler2 + ' 3 ' + ruler2
    ruler4 = ruler3 + ' 4 ' + ruler3

    stdio.writeln(ruler1)
    stdio.writeln(ruler2)
    stdio.writeln(ruler3)
    stdio.writeln(ruler4)


if __name__ == '__main__':
    main()