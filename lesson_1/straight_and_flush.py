# -----------
# User Instructions
#
# Define two functions, straight(ranks) and flush(hand).
# Keep in mind that ranks will be ordered from largest
# to smallest.


def straight(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return reduce(lambda x, y: y if (x == y+1) else False, ranks) == ranks[-1]


def straight_pn(ranks):
    "Return True if the ordered ranks form a 5-card straight."
    return (max(ranks)-min(ranks) == 4) and len(set(ranks)) == 5


def flush(hand):
    "Return True if all the cards have the same suit."
    return all(s[1] == hand[0][1] for s in hand)


def flush_pn(hand):
    "Return True if all the cards have the same suit."
    suits = [s for r,s in hand]
    return len(set(suits)) == 1


def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()
    fk = "9D 9H 9S 9C 7D".split()
    fh = "TD TC TH 7C 7D".split()
    assert flush(sf) == True
    assert flush(fk) == False
    assert straight([9, 8, 7, 6, 5]) == True
    assert straight([9, 8, 8, 6, 5]) == False
    return 'tests pass'

print test()