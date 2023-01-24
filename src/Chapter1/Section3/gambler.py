#----------------------------------------
# Program 1.3.8 Gambler's ruin simulation
# (gambler.py)
# Eric/a Seyden
# ---------------------------------------

import random
import sys
import stdio

def main(arg1, arg2, arg3):
    stake = int(arg1)
    goal = int(arg2)
    trials = int(arg3)

    bets = 0
    wins = 0
    for t in range(trials):
        cash = stake
        while (cash > 0) and (cash < goal):
            bets += 1
            if random.randrange(0, 2) == 0:
                cash += 1
            else:
                cash -= 1
        if cash == goal:
            wins +=1
    
    stdio.writeln(str(100 * wins // trials) + '% wins')
    stdio.writeln('Avg # bets: ' + str(bets // trials))

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3])
