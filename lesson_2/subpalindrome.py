# --------------
# User Instructions
#
# Write a function, longest_subpalindrome_slice(text) that takes
# a string as input and returns the i and j indices that
# correspond to the beginning and end indices of the longest
# palindrome in the string.
#
# Grading Notes:
#
# You will only be marked correct if your function runs
# efficiently enough. We will be measuring efficency by counting
# the number of times you access each string. That count must be
# below a certain threshold to be marked correct.
#
# Please do not use regular expressions to solve this quiz!


def advance_iteration(N):
    i, j = 0, 1
    while j < N:
        yield i,j
        j += 1
        if j == N:
            break
        yield i,j
        i += 1
        if i == N:
            break


def grow_iteration(x1, x2, N):
    i, j = x1, x2
    while True:
        i, j = i-1, j+1
        if i == -1 or j == N:
            break
        else:
            yield i, j


def grow(text, x1, x2):
    lmax, rmax = x1, x2
    for i,j in grow_iteration(x1, x2, len(text)):
        if text[i] == text[j] or text[i].lower() == text[j].lower():
            lmax, rmax = i, j
        else:
            break
    return lmax, rmax


def longest_subpalindrome_slice(text):
    "Return (i, j) such that text[i:j] is the longest palindrome in text."
    m, lmmax, rmmax = len(text), 0, 0
    for i, j in advance_iteration(m):
        lmax, rmax = 0, 0
        if text[i] == text[j] or text[i].lower() == text[j].lower():
            lmax, rmax = grow(text, i, j)
            rmax += 1
        if abs(rmax - lmax) > abs(rmmax - lmmax):
            lmmax, rmmax = lmax, rmax
    return lmmax, rmmax


def test():
    L = longest_subpalindrome_slice
    assert L('racecar') == (0, 7)
    assert L('Racecar') == (0, 7)
    assert L('RacecarX') == (0, 7)
    assert L('Race carr') == (7, 9)
    assert L('') == (0, 0)
    assert L('something rac e car going') == (8, 21)
    assert L('xxxxx') == (0, 5)
    assert L('Mad am I ma dam.') == (0, 15)
    return 'tests pass'


print(test())