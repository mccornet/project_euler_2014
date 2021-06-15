from tools import pyprimes
import itertools

'''
The arithmetic sequence, 1487, 4817, 8147,
in which each of the terms increases by 3330,
is unusual in two ways: (i) each of the three
terms are prime, and, (ii) each of the
4-digit numbers are permutations of one another.

There are no arithmetic sequences made
up of three 1-, 2-, or 3-digit primes,
exhibiting this property, but there is
one other 4-digit increasing sequence.

What 12-digit number do you form by
concatenating the three terms in this sequence?
'''
# prime generator
prime_gen = pyprimes.primes_above(1000)

primes = [] # all primes that are of concern


prime_permutations = dict() # contains all primes that are permutations of each other, stored under string representation

# store primes from 1000 to 10000
while True:
    next_prime = next(prime_gen)

    if next_prime > 10000:
        break

    primes.append(next_prime)

# process each prime. mapping relation between string representation and prime
# and grouping primes with matching string representation together

for prime in primes:

    # sort to recognize permutation
    key = ''.join(sorted(str(prime)))

    # update dictionary
    if key in prime_permutations :
        prime_list = prime_permutations[key]
        prime_list.append(prime)
    else:
        prime_permutations[key] = [prime]

for candidate in prime_permutations.items():

    # print(candidate[1])
    # DETECT IF IT CONTAINS A ARITMETIC SEQ
    subsets = itertools.combinations(candidate[1], 3)

    for subset in list(subsets):
        if subset[2] - subset[1] == subset[1] - subset[0]:
            print('a valid solution: ', subset, ', ',str(subset[0]),str(subset[1]),str(subset[2]))

