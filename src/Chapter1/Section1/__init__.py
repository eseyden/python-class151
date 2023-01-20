__all__ = ["helloworld", "helloworld10", "useargument", "usethree"]
from Chapter1.Section1 import *


def main():
    print("\nProgram 1.1.1\nHello, World\n")
    helloworld.main()

    print("\nProgram 1.1.2\nUsing a command-line argument\n")
    useargument.main('Dave')

    print("\nExercise 1.1.1 Compose a program that writes the Hello, World message 10 times.\n")
    helloworld10.main()

    print("\nExercise 1.1.6\n" + \
          "Modify useargument.py to compose a program usethree.py\n" +
          "that takes three names and writes a proper sentence\n" +
          "with the names in the reverse of the order they are given,\n" +
          "so that, for example, python usethree.py Alice Bob Carol\n" +
          "writes the string 'Hi Carol, Bob, and Alice'..\n")
    usethree.main('Carol', 'Bob', 'Alice')