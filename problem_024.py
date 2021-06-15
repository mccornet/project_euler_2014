# What is the millionth lexicographic permutation
# of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

import itertools
permutations = itertools.permutations(range(0,10)) # generator

perm = 0;
for x in range(10**6):
    perm = next(permutations)

print(perm)