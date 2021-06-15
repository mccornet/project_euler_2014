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

prime_string_cnt = dict()  # mapping how much permutations there are of a certain prime in string format

string_to_primes = dict() # storing primes under their sorted permutation key

prime_permutations = dict() # contains tuple of all primes that are permutations of each other
prime_permutation_keys = [] # keys to this dictionary


# store primes from 1000 to 10000
while True:
    next_prime = next(prime_gen)

    if next_prime > 10000:
        break

    primes.append(next_prime)


for prime in primes:

    # sort to recognize permutation
    sorted_str_prime = ''.join(sorted(str(prime)))

    # store under the
    string_to_primes[prime] = sorted_str_prime

    if sorted_str_prime in prime_string_cnt:
        value = prime_string_cnt[sorted_str_prime]
        value +=1

        if value >= 3:

            keys = sorted([key for key,value in string_to_primes.items() if value==sorted_str_prime ])

            prime_permutations[keys[0]] = keys

            if value == 3: prime_permutation_keys.append(keys[0])

        prime_string_cnt[sorted_str_prime] = value

    else:
        prime_string_cnt[sorted_str_prime] = 1

#print(prime_permutation_keys)

for elem in prime_permutation_keys:

    # print(prime_permutations[elem])
    # DETECT IF IT CONTAINS A ARITMETIC SEQ

    subsets = itertools.combinations(prime_permutations[elem], 3)

    for subset in list(subsets):
        if subset[2] - subset[1] == subset[1] - subset[0]:
            print('a valid solution: ', subset)


for candidate in prime_permutations.items():

    print(candidate[1])
    # DETECT IF IT CONTAINS A ARITMETIC SEQ

    subsets = itertools.combinations(candidate[1], 3)

    for subset in list(subsets):
        if subset[2] - subset[1] == subset[1] - subset[0]:
            print('a valid solution: ', subset)

