# -----------
# User Instructions
#
# Define a function, two_pair(ranks).


def two_pair(ranks):
    """If there are two pair, return the two ranks as a
    tuple: (highest, lowest); otherwise return None."""
    p = kind(2, ranks)
    nr = kind(2, [r for r in ranks if r != p]) if p else None
    if nr:
        return p, nr
    else:
        return None


def two_pair_pn(ranks):
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair and lowpair != pair:
        return pair, lowpair
    else:
        return None


def kind(n, ranks):
    """Return the first rank that this hand has exactly n of.
    Return None if there is no n-of-a-kind in the hand."""
    for r in ranks:
        if ranks.count(r) == n: return r
    return None


def test():
    "Test cases for the functions in poker program."
    sf = "6C 7C 8C 9C TC".split()  # Straight Flush
    fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
    fh = "TD TC TH 7C 7D".split()  # Full House
    tp = "5S 5D 9H 9C 6S".split()  # Two pairs
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)
    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == (9,5)
    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7
    return 'tests pass'


def card_ranks(hand):
    "Return a list of the ranks, sorted with higher first."
    ranks = ['--23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    return ranks


print test()