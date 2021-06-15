# calculate nr of non bouncy numbers below 10^100

from itertools import product

def binom(n,k):
    """ Returns binomial coefficients using multiplicative formula """
    # http://en.wikipedia.org/wiki/Binomial_coefficient
    res = 1
    for i in range(1,k+1):
        res *= (n-i+1)/i

    return int(round(res,0))

# 10^power is the given upper limit
power_10 = 100

# n_max: nr digits considered - 1. 
# limit 10^2 = 100 > 99 max = 2 digits, represented by lattice path 0,9 to 1,9
n_max = power_10-1

# sum all possible latice paths going up from 0.0 to 1.1, 1.2, 1.3, ..., 1.9 
sum_up = 0
for i in range(1,10):
    sum_up += binom(n_max+i,i)

# sum all possible paths down. 
# leading zeros are allowed vb: 
# lattice path wont come across 090 when n_ max = 3, 
# which is the same as 90 when n_max = 2
# so n must also be summated for all smaller possible n's
sum_down = 0
for n_i in product(range(1,n_max+1),range(1,10)):

    n, i = n_i[0], n_i[1]
    sum_down += binom(n+i,i)

# doubles, all 'flat' lines in the lattice paths, vb: 1, 11, 111, 9999
# 9 flat paths per digit, except 1,2,3,4,5,6,7,8,9 
# but sum down starts at 2 digits so n_max works
doubles = 9*n_max

print(sum_up+sum_down-doubles)

