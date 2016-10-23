import itertools
houses = [1,2,3,4,5]
perms = itertools.permutations(houses)


def all_ints():
    "Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."
    i, previous = 0, 0
    while True:
        if previous > 0:
            previous *= -1
            yield previous
        else:
            yield i
            previous = i
            i += 1


def all_ints_pn():
    yield 0
    i = 1
    while True:
        yield +i
        yield -i
        i += 1

g =all_ints_pn()
print next(g)
print next(g)
print next(g)
print next(g)
print next(g)
print next(g)
print next(g)
