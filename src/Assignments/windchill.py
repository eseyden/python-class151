# ----------------------------------------------------
# Assignment #2
# Exercise 1.2.22 Wind chill
# ( windchill.py )
# Eric(a) Seyden
# 2023-01-20
# -----------------------------------------------------

import sys
import stdio


def main(arg1, arg2):  # command line main function
    temperature = float(arg1)  # parse first argument as float
    wind_speed = float(arg2)  # parse second argument as float
    # calculate wind chill
    wind_chill = 35.74 + (0.6215 * temperature) + (((0.4275 * temperature) - 35.75) * (wind_speed ** 0.16))

    # write out results
    stdio.writeln("Temperature = " + str(temperature))
    stdio.writeln("Wind speed  = " + str(wind_speed))
    stdio.writeln("Wind chill  = " + str(wind_chill))


if __name__ == "__main__":  # check if script is called directly
    main(sys.argv[1], sys.argv[2])  # call main with command line arguments
