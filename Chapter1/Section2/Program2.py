import sys
import stdio


def run(arg1, arg2):
    a = int(arg1)
    b = int(arg2)

    total = a + b
    diff = a - b
    prod = a * b
    quot = a // b
    rem = a % b
    exp = a ** b

    stdio.writeln(str(a) + ' +  ' + str(b) + ' = ' + str(total))
    stdio.writeln(str(a) + ' -  ' + str(b) + ' = ' + str(diff))
    stdio.writeln(str(a) + ' *  ' + str(b) + ' = ' + str(prod))
    stdio.writeln(str(a) + ' // ' + str(b) + ' = ' + str(quot))
    stdio.writeln(str(a) + ' %  ' + str(b) + ' = ' + str(rem))
    stdio.writeln(str(a) + ' ** ' + str(b) + ' = ' + str(exp))


if __name__ == "__main__":
    run(sys.argv[1], sys.argv[2])