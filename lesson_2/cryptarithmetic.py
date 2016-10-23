# -------------
# User Instructions
#
# Complete the fill_in(formula) function by adding your code to
# the two places marked with ?????.

from __future__ import division, print_function
import string, re, itertools, time
import cProfile

file=open("logs/main.txt", 'a')

def compile_word_cbrr(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+') => '+'"""
    return sum([10**idx for idx, x in enumerate(reversed(''.join(re.findall("[A-Z]+", word))))])


def compile_word(word):
    if word.isupper():
        terms = [('%s*%s' % (10**i, d))
                 for (i,d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
    else:
        return word


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    for idx, f in enumerate(fill_in(formula)):
        if valid(f):
            pass

def fill_in(formula):
    "Generate all possible fillings-in of letters in formula with digits."
    letters = ''.join(set(re.findall("[A-Z]", formula)))
    for digits in itertools.permutations('1234567890', len(letters)):
        table = string.maketrans(letters, ''.join(digits))
        yield formula.translate(table)


def valid(f):
    """Formula f is valid if and only if it has no
    numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ArithmeticError:
        return False


def faster_solve(formula):
    """"""
    f, letters = compile_formula(formula, True)
    for digits in itertools.permutations((1,2,3,4,5,6,7,8,9,0), len(letters)):
        try:
            if f(*digits) is True:
                table = string.maketrans(letters, ''.join(map(str, digits)))
                formula.translate(table)
        except ArithmeticError:
            pass

def compile_formula_first_no_leading_zeros(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
        in same order as params function. For example, 'YOU == ME**2'
        :returns (lambda Y,M,E,U,O: (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO' """
    """
        THIS IS WRONG BECAUSE IT FINDS ANY ZERO AND RETURNS FALSE
        CORRECT BEHAVIOR: LEADING VAR IN ARGUMENT IS 0. EXAMPLES:
        YOU -> 012
        PEPE -> 0505
        CUP -> 087
        COSO + CAP == CIT -> 0939 + 053 == 078
        ONLY IF THE FIRST INT IS ZERO SHOULD BE FALSE
    """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    f = 'lambda %s: %s if not 0 in [%s] else False' % (parms, body, parms)
    if verbose: print(f)
    return eval(f), letters

def compile_formula(formula, verbose=False):
    """Compile formula into a function. Also return letters found, as a str,
        in same order as params function. For example, 'YOU == ME**2'
        :returns (lambda Y,M,E,U,O: (U+10*O+100*Y) == (E+10*M)**2), 'YMEUO' """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    firstletters = set(re.findall(r'\b([A-Z])[A-Z]', formula)) # This extracts the first letter in every word
    parms = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = ''.join(tokens)
    if firstletters:
        test = ' and '.join(L+'!=0' for L in firstletters)
        body = '%s and (%s)' % (test, body)
    f = 'lambda %s: %s' % (parms, body)
    if verbose: print(f)
    return eval(f), letters

examples = """YOU == ME**2
TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN""".splitlines()

examples_complete = """YOU == ME**2
TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
PLUTO not in set([PLANETS])""".splitlines()

""" Removed:
    GLITTERS is not GOLD
    ONE < TWO and FOUR < FIVE
    PLUTO not in set([PLANETS])"""

def timedcall(fn, *args):
    """ Call function and return elapsed time """
    t0 = time.clock()
    res = fn(*args)
    t1 = time.clock()
    return t1 - t0, res

def test(function, dataset):
    t0 = time.clock()
    for example in dataset:
        print(); print(13*' ', example)
        print('%6.4f sec:   %s ' % timedcall(function, example))
    print('%6.4f tot.' % (time.clock()-t0))


#test(solve, examples)
cProfile.run('test(faster_solve, examples_complete)')