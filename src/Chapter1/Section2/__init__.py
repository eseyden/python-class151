__all__ = ["ruler", "floatops", "intops", "quadratic", "leapyear", "stats", "stats2", "threesort"]

from Chapter1.Section2 import *


def run_all():
    print("\nProgram 1.2.1\nString concatenation example\n\npython ruler.py")
    ruler.main()

    print("\nProgram 1.2.2\nInteger operators\n\npython intops.py 1234 5")
    intops.main(1234, 5)

    print("\nProgram 1.2.3\nFloat operators\n\npython floatops.py 123.456 78.9")
    floatops.main(123.456, 78.9)

    print("\nProgram 1.2.4\nQuadratic formula\n\npython quadratic.py -3.0 2.0")
    quadratic.main(-3.0, 2.0)
    print("\npython quadratic.py -1.0 -1.0")
    quadratic.main(-1.0, -1.0)
    print("\npython quadratic.py 1.0 1.0")
    try:
        quadratic.main(1.0, 1.0)
    except ValueError as inst:
        print("ValueError: " + str(inst))

    print("\nProgram 1.2.3\nLeap year\n\npython leapyear.py 2016")
    leapyear.main(2016)
    print("\npython leapyear.py 1900")
    leapyear.main(1900)
    print("\npaython leapyear.py 2000")
    leapyear.main(2000)

    print("\nExercise 1.2.27\nUniform random numbers\n\npython stats.py")
    stats.main()

    print("\nExercise 1.2.31\nThree-sort\n\npython threesort.py 175 250 10")
    threesort.main(175, 250, 10)
