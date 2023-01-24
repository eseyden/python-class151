# ------------------------------------------------
# Exercise 1.2.31 Three-sort
# ( threeint.py )
# Eric/a Seyden
# 2023-01-20
# Quick in class implementation statement
# ------------------------------------------------


import sys
import stdio

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])

if a > b and a > c:
    if b > c:
        stdio.writeln(c)
        stdio.writeln(b)
    else:
        stdio.writeln(b)
        stdio.writeln(c)
    stdio.writeln(a)
elif b > c and b > a:
    if c > a:
        stdio.writeln(a)
        stdio.writeln(c)
    else:
        stdio.writeln(c)
        stdio.writeln(a)
    stdio.writeln(b)
else:
    if a > b:
        stdio.writeln(b)
        stdio.writeln(a)
    else:
        stdio.writeln(a)
        stdio.writeln(b)
    stdio.writeln(c)

my_list = [a, b, c]
my_list.sort()

stdio.writeln(str(my_list[0]) + " " + str( my_list[1]) + " " + str( my_list[2]))
