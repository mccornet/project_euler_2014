# Find the sum of all the primes below two million.

from tools import pyprimes

primestream = pyprimes.primes()
primesum = 0

while True:
    prime = next(primestream)

    if prime > 2*10**6:
        break;

    primesum += prime

print("the sum of the primes below 2 million: {}".format(primesum))

