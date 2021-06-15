import itertools
from tools import pyprimes

number = 0

"""
We shall say that an n-digit number is pandigital if it makes use of
all the digits 1 to n exactly once. For example,

2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

# numbers whose sum of individual digits is divisable by three is divisable by three
# 12345678 is divisable by 3
# 123456789 is diviable by 3
# this makes the max a permutation of 7654321

# using string premutations
for perm in itertools.permutations("7654321"):

    p = int("".join(perm)) # permutation is individual elements

    if pyprimes.isprime(p):
        print(p)
        #permutation goes down, first number is highest
        break

# using list permutation
for perm in itertools.permutations(range(7,0,-1)):

    # very cheap first check if not prime
    if perm[-1] % 2 == 0: continue

    # if the list represents an integer we can determine the integer
    # this is done by multiplying each element with the corresponding 10th power of that position.
    p = 0
    for i in range(0, len(perm)):
        p += perm[i]*10**(len(perm)-1-i)

    if pyprimes.isprime(p):
        print(p)
        break

