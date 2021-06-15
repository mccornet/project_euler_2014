"""
The number 145 is well known for the property 
that the sum of the factorial of its digits 
is equal to 145:

    1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces
the longest chain of numbers that link back to 169; 
it turns out that there are only three such loops 
that exist:

    169 → 363601 → 1454 → 169
    871 → 45361 → 871
    872 → 45362 → 872

It is not difficult to prove that EVERY starting number 
will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms,
but the longest non-repeating chain with a starting number 
below one million is sixty terms.

How many chains, with a starting number below one million,
contain exactly sixty non-repeating terms?

"""
from math import factorial

cached_factorials = [factorial(n) for n in range(10)]

def digit_factorial_sum(n):
    """ computes the sum of the individual digits factorial """

    factorial_sum = 0

    while n:
        digit = n%10
        factorial_sum += cached_factorials[digit]
        n //= 10

    return factorial_sum

def chain_length_vebose(n):

    sums = set()
    sums.add(n)

    while True:
        print(n)
        n = digit_factorial_sum(n)
        if n in sums : break
        sums.add(n)

    return len(sums)

non_solutions = set()

def chain_length(n):

    if n in non_solutions: return 0

    sums = set()
    sums.add(n)

    while True:
        n = digit_factorial_sum(n)
        
        # max length is 60, so every encountered digit 
        # beyond the starting point is definitly not a solution
        non_solutions.add(n)
        
        if n in sums : break
        sums.add(n)

    return len(sums)

def nr_60_len_chain():

    chain_60 = []

    for start_nr in range(1,1000000):
        l = chain_length(start_nr)

        if l == 60 : chain_60.append(start_nr)

    return chain_60

res = nr_60_len_chain()

print(len(res))
