# ------------------------------------------------
# Exercise 1.2.27 Uniform random numbers
# ( stats2.py )
# Eric/a Seyden
# 2023-01-20
# ------------------------------------------------

import stdio
import random


def main():
    # initialize random values for five numbers
    number1 = random.uniform(0.0, 0.1)
    number2 = random.uniform(0.0, 0.1)
    number3 = random.uniform(0.0, 0.1)
    number4 = random.uniform(0.0, 0.1)
    number5 = random.uniform(0.0, 0.1)

    # calculate average
    number_sum = (number1 + number2 + number3 + number4 + number5)
    average = number_sum / 5

    # find minimum and maximum
    minimum = min(number1, number2, number3, number4, number5)
    maximum = max(number1, number2, number3, number4, number5)

    # output results
    stdio.writeln("Number 1 : " + str(number1))
    stdio.writeln("Number 2 : " + str(number2))
    stdio.writeln("Number 3 : " + str(number3))
    stdio.writeln("Number 4 : " + str(number4))
    stdio.writeln("Number 5 : " + str(number5))
    stdio.writeln("Average  : " + str(average))
    stdio.writeln("Minimum  : " + str(minimum))
    stdio.writeln("Maximum  : " + str(maximum))


if __name__ == "__main__":  # check if package is called via command line and run main function
    main()  # run main function
