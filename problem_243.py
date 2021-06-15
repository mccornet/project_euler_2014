from tools import pyprimes

"""
A positive fraction whose numerator is less than 
its denominator is called a proper fraction.

For any denominator, d, there will be d−1 proper 
fractions; for example, with d = 12:

1/12 , 2/12 , 3/12 , 4/12 , 5/12 , 6/12 , 7/12 , 8/12 , 9/12 , 10/12 , 11/12 .

We shall call a fraction that cannot be cancelled down a resilient fraction.

Furthermore we shall define the resilience of a denominator, R(d), 
to be the ratio of its proper fractions that are resilient; 
for example, R(12) = 4/11 .

In fact, d = 12 is the smallest denominator having a resilience R(d) < 4/10 .

Find the smallest denominator d, having a resilience R(d) < 15499/94744 .
"""

TARGET_RESILIENCE = 4/10

# Resilience is given by phi(n) / n-1
prime_gen = pyprimes.primes()

primes = []
for i in range(10000):
    primes.append(next(prime_gen))

prod = 1
index = 0

while prod > 1/10:
    prod *= (1-(1/primes[index]))
    index +=1

print(prod)

print("nr of primes needed:",index-1)
