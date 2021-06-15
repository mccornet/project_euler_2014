import functools
from tools import pyprimes
'''
Starting with 1 and spiralling anticlockwise in the following way,
a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares
lie along the bottom right diagonal, but what
is more interesting is that 8 out of the 13 numbers
lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above
, a square spiral with side length 9 will be formed.
If this process is continued, what is the side length
of the square spiral for which the ratio of primes
along both diagonals first falls below 10%?
'''

# top right corner: 1,9,25,49
# n**2 for n = 1,3,5,7 .... 1001
# the other corners decrease with n-1
#
# so ring corner values diag n
# are given by
#
# SUM( n**2 - (n-1)*m ) m = 0,1,2,3

#diag_sum = 1
#for n in range(3,1002,2):
#    t1 = n**2
#    t2 = n-1
#    diag_sum += 4*t1 - 6*t2

# corners for side length n [(n**2-(n-1)*m) for m in range(0,4)]
# n: 3,5,7,9

# create set of corners and check percentage prime

nr_corners = 1
nr_prime_corners = 0

n = 1
percentage = 1.0

while percentage >= 0.1:

    #next side
    n += 2

    # new nr corners
    nr_corners += 4

    # add corners to set
    for corner in [(n**2-(n-1)*m) for m in range(0,4)]:
        if pyprimes.isprime(corner):
            nr_prime_corners += 1

    # we only counted corners
    percentage = nr_prime_corners / nr_corners

    #print(n)
    #print(percentage)

print("percentage is: {} for n: {}".format(percentage,n))
