# ------------------------------------------------
# Exercise 1.2.27 Uniform random numbers
# ( stats2.py )
# Eric/a Seyden
# 2023-01-20
# ------------------------------------------------
import sys
import random
import stdio
import statistics
# used for experiment in float precision printing
import decimal
extra_precision = False  # global flag for printing float as decimal


def main():  # main program, runs by default when called from command line
    numbers = []  # initialize an array
    for count in range(0, 5):  # loop 5 times
        numbers.append(get_random_float())  # add the return value of get_random_float to the array

    average = statistics.mean(numbers)  # calculate the average
    minimum = min(numbers)  # calculate minimum
    maximum = max(numbers)  # calculate maximum

    for count, number in enumerate(numbers):  # iterate over the number array and provide a loop counter
        # print out a float converted to string
        stdio.writeln("Number " + str(count + 1) + " : " + convert_to_string(number))

    stdio.writeln("Average  : " + convert_to_string(average))  # print average
    stdio.writeln("Minimum  : " + convert_to_string(minimum))  # print minimum
    stdio.writeln("Maximum  : " + convert_to_string(maximum))  # print maximum


def get_random_float():  # generate a random float between 0.0 and 1.0
    return random.uniform(0.0, 1.0)


def convert_to_string(number):  # format float for printing
    if not extra_precision:  # check to see if extra precision is wanted
        return str(number)
    return str(decimal.Decimal.from_float(number))  # Does this much larger float precision actually exist?


if __name__ == "__main__":  # check if package is called via command line and run main function
    for argument in sys.argv:  # loop through command line arguments
        if argument == "--extra":  # check for command line argument
            extra_precision = True  # enable decimal float representation
    main()  # run main function
