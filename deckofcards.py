import stdio
import random

SUITS = ["Clubs", "Diamonds", "Hearts","Spades"]
RANKS = ["2","3","4","5","6","7","8","9","10","Jack","Queen","King","Ace"]

deck = []

for suit in SUITS:
    for rank in RANKS:
        deck += [rank + " of " + suit]

start_deck = deck[:]
stdio.writeln(start_deck)
shuf_deck = []

while len(start_deck) > 0:
    pluck = random.randrange(0,len(start_deck))
    shuf_deck += [start_deck.pop(pluck)]

stdio.writeln(shuf_deck)
