# ----------------------------------------------------
# Assignment #2
# Exercise 1.2.22 Wind chill
# ( windchill.py )
# Eric(a) Seyden
# 2023-01-20
# -----------------------------------------------------

import sys
import stdio


def main(arg1, arg2):
    temperature = float(arg1)
    wind_speed = float(arg2)
    wind_chill = 35.74 + (0.6215 * temperature) + (((0.4275 * temperature) - 35.75) * (wind_speed ** 0.16))

    stdio.writeln("Temperature = " + str(temperature) )
    stdio.writeln("Wind speed  = " + str(wind_speed) )
    stdio.writeln("Wind chill  = " + str(wind_chill))


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
