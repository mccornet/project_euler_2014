from tools import pyprimes

'''
It was proposed by Christian Goldbach
that every odd composite number can
be written as the sum of a prime and twice a square.

9  = 7  + 2×1^2
15 = 7  + 2×2^2
21 = 3  + 2×3^2
25 = 7  + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be
written as the sum of a prime and twice a square?
'''

prime_gen = pyprimes.primes()
primes  = []
primes.append(next(prime_gen))

# precalculate set of squares
squares = set([2*n**2 for n in range(1,1000)])
# baundary
max_square = 2*999**2

#for elem in [2*n**2 for n in range(1,1000)]: squares.add(elem)

odd_nr = 7

# we have not found any disputing proof
proof = 0

while not proof:

    # next odd number
    odd_nr += 2

    # fault check, assumption is that we calculated enough sqaures
    if odd_nr > max_square: print("error")

    # generate extra primes
    while odd_nr >= primes[-1] : primes.append(next(prime_gen))

    # if odd number turned out prime try next odd number
    if(odd_nr in primes): continue

    # at this point we have non prime odd number, with all the smaller primes...

    proof = 1 # assume current number will prove the conjecture to be false

    # subtract smaller prime from the odd number
    # if the difference is a square: reset proof and skip
    # the latest prime number is always bigger than the odd number: len()-1
    # try this for all smaller primes if needed
    for i in range(len(primes)-1,0,-1):

        delta = odd_nr - primes[i]

        if delta in squares:
            proof = 0  # current nummer turned out to be no proof
            break      # stop this search


print(odd_nr)
