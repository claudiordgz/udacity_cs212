# -----------
# User Instructions
#
# Write a function, deal(numhands, n=5, deck), that
# deals numhands hands with n cards each.
#

import random  # this will be a useful library for shuffling

# This builds a deck of 52 cards. If you are unfamiliar
# with this notation, check out Andy's supplemental video
# on list comprehensions (you can find the link in the
# Instructor Comments box below).

mydeck = [r + s for r in '23456789TJQKA' for s in 'SHDC']


def deal(numhands, n=5, deck=mydeck):
    # Your code here.
    random.shuffle(deck)
    return [deck[x:x + n] for idx, x in enumerate(range(0, len(deck), n)) if idx < numhands]

def deal_pn(numhands, n=5, deck=mydeck):
    # Your code here.
    random.shuffle(deck)
    return [deck[i*n:n*(i+1)] for i in range(numhands)]


print deal_pn(4)