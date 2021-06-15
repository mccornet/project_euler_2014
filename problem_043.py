import itertools
import functools

"""
The number, 1406357289, is a 0 to 9 pandigital number because
it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on.
In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""


permutations = itertools.permutations(range(0,10)) # generator of all pandigital numbers
perm_list = []

for perm in permutations:
    # NB, d1 is perm[0]

    # d4d5d6 disivable by 5 => d6 is 0 of 5
    if not ( perm[5] == 0 or perm[5] == 5 ): continue

    # d2d3d4 divisable by 2 => d4 a multiple of 2
    if not ( perm[3] % 2 == 0 ): continue

    # sum of number /3 > number /3
    if not ( (perm[2]+perm[3]+perm[4]) % 3 == 0): continue

    if not ( (perm[4]*100+perm[5]*10+perm[6]) % 7 == 0): continue

    if not ( (perm[5]*100+perm[6]*10+perm[7]) % 11 == 0): continue

    if not ( (perm[6]*100+perm[7]*10+perm[8]) % 13 == 0): continue

    if not ( (perm[7]*100+perm[8]*10+perm[9]) % 17 == 0): continue

    # made it past all checks!
    print(perm)
    perm_list.append(perm)


sum_p = 0

for p in perm_list:

    # tuple to integer conversion and addition
    for i in range(0,10):
        sum_p += p[i]*10**(9-i)

print(sum_p)
