# --------------
# User Instructions
#
# Write a function, inverse, which takes as input a monotonically
# increasing (always increasing) function that is defined on the
# non-negative numbers. The runtime of your program should be
# proportional to the LOGARITHM of the input. You may want to
# do some research into binary search and Newton's method to
# help you out.
#
# This function should return another function which computes the
# inverse of the input function.
#
# Your inverse function should also take an optional parameter,
# delta, as input so that the computed value of the inverse will
# be within delta of the true value.

# -------------
# Grading Notes
#
# Your function will be called with three test cases. The
# input numbers will be large enough that your submission
# will only terminate in the allotted time if it is
# efficient enough.

from tools import trace

def binary_search(f, y, lo, hi, delta):
    while lo <= hi:
        x = (lo + hi) / 2.;
        if f(x) < y:
            lo = x + delta
        elif f(x) > y:
            hi = x - delta
        else:
            return x
    return hi if (f(hi)-y < y-f(lo)) else lo


def inverse(f, delta=1 / 128.):
    """Given a function y = f(x) that is a monotonically increasing function on
    non-negatve numbers, return the function x = f_1(y) that is an approximate
    inverse, picking the closest value to the inverse, within delta."""
    def find_bounds(f, y):
        x = 1.
        while f(x) < y:
            x = x * 2
        lo = 0 if (x == 1) else x/2.
        return lo,x

    def f_1(y):
        lo, hi = find_bounds(f, y)
        return binary_search(f, y, lo, hi, delta)

    return f_1

#@trace
def square(x): return x * x

#@trace
def power10(x): return 10**x

#@trace
def cuber(x): return x*x*x

log10 = inverse(power10)

sqrt = inverse(square)

cuberoot = inverse(cuber)

def test():
    import math
    nums = [2,4,6,8,10,99,100,101,1000,10000,20000,40000,100000000]
    for n in nums:
        test1(n, 'sqrt', sqrt(n), math.sqrt(n))
        test1(n, 'log', log10(n), math.log10(n))
        test1(n, '3-rt', cuberoot(n), n**(1./3.))


def test1(n, name, value, expected):
    diff = abs(value-expected)
    print '%6g: %s = %13.7f (%13.7f actual); %.4f diff; %s' % (
        n, name, value, expected, diff,
        ('ok' if diff < 0.002 else '**** BAD ****')
    )


if __name__ == '__main__':
    print sqrt(1000000000)
    test()