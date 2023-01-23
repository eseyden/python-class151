# ------------------------------------------------
# Program 1.3.1 Flipping a fair coin
# ( flip.py )
# Eric/a Seyden
# 2023-01-21
# ------------------------------------------------

import random
import stdio


def main():
    if random.randrange(0, 2) == 0:
        stdio.writeln('Heads')
    else:
        stdio.writeln('Tails')


if __name__ == "__main__":
    main()
