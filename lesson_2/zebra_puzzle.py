import itertools


def imright(h1,h2):
    """ House h1 is to the right of h2 if h1-h2 == 1 """
    return h1 - h2 == 1


def nextto(h1,h2):
    """ Two houses are next to each other if they differ by 1 """
    return abs(h1-h2) == 1

def zebra_puzzle_exhaustive():
    houses = first, _, middle, _, _ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in c(orderings)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
                for (dog, snails, fox, horse, ZEBRA) in c(orderings)
                for (coffee, tea, milk, oj, WATER) in c(orderings)
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
                if Englishman is red
                if Spaniard is dog
                if coffee is green
                if Ukranian is tea
                if imright(green, ivory)
                if OldGold is snails
                if Kools is yellow
                if milk is middle
                if Norwegian is first
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                if LuckyStrike is oj
                if Japanese is Parliaments
                if nextto(Norwegian, blue)
                )

def zebra_puzzle():
    houses = first, _, middle, _, _ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)
                for (red, green, ivory, yellow, blue) in c(orderings)
                if imright(green, ivory)
                for (Englishman, Spaniard, Ukranian, Japanese, Norwegian) in c(orderings)
                if Englishman is red
                if Norwegian is first
                if nextto(Norwegian, blue)
                for (coffee, tea, milk, oj, WATER) in c(orderings)
                if coffee is green
                if Ukranian is tea
                if milk is middle
                for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
                if Kools is yellow
                if LuckyStrike is oj
                if Japanese is Parliaments
                for (dog, snails, fox, horse, ZEBRA) in c(orderings)
                if Spaniard is dog
                if OldGold is snails
                if nextto(Chesterfields, fox)
                if nextto(Kools, horse)
                )


import time


def timedcall(fn, *args):
    """ Call function and return elapsed time """
    t0 = time.clock()
    res = fn(*args)
    t1 = time.clock()
    return t1 - t0, res



def timedcalls(n, fn, *args):
    """Call fn(*args) repeatedly: n times if n is an int, or up to
        n seconds if n is a float; return the min, avg, and max time"""
    if isinstance(n, int):
        times = [timedcall(fn, *args)[0] for _ in range(n)]
    else:
        times = []
        while sum(times) < n:
            times.append(timedcall(fn, *args)[0])
    return min(times), average(times), max(times)


def average(numbers):
    "Return the average (arithmetic mean) of a sequence of numbers."
    return sum(numbers) / float(len(numbers))

def ints(start, end):
    i = start
    while i <= end:
        yield i
        i = i + 1

def c(sequence):
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item

def instrument_fn(fn, *args):
    c.starts, c.items = 0, 0
    result = fn(*args)
    print('%s got %s with %5d iters over %7d items' % (
        fn.__name__, result, c.starts, c.items
    ))

instrument_fn(zebra_puzzle)


instrument_fn(zebra_puzzle_exhaustive)