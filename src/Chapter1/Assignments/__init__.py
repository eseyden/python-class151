__all__ = ["compound", "windchill"]

from Chapter1.Assignments import *


def run_all():
    print("Assignment #1\nExercise 1.2.21\n\npython compound.py 2 1500 .04")
    compound.main(2, 1500, .04)
    print("\npython compound.py 10 1500 .04")
    compound.main(10, 1500, .04)