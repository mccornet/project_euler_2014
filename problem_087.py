"""
How many numbers below fifty million can 
be expressed as the sum of a prime square, 
prime cube, and prime fourth power?
"""
from tools import pyprimes
import itertools

def scq_primes(target):
    "returns squares, cubes and quads of primes till target is reached"
    prime_gen = pyprimes.primes()

    prime_2, prime_3, prime_4 = [], [], []

    cont_2 = cont_3 = cont_4 = True

    while cont_2 or cont_3 or cont_4:

        p = next(prime_gen)

        if cont_2:
            if p**2 > target:
                cont_2 = False
            else:
                prime_2.append(p**2)

        if cont_3:
            if p**3 > target: 
                cont_3 = False
            else: 
                prime_3.append(p**3)

        if cont_4:
            if p**4 > target:
                cont_4 = False
            else:
                prime_4.append(p**4)

    return prime_2, prime_3, prime_4

def problem_87():

    target = 50000000
    combinations = set()
    prime_2, prime_3, prime_4 = scq_primes(target)

    # TRY ALL THE POSSIBILITIES!
    a = [prime_2, prime_3, prime_4]
    for p in itertools.product(*a):
        prime_sum = sum(p)
        if prime_sum <= target : 
            combinations.add(prime_sum)

    """ THIS IS SLIGHTLY FASTER
    for p4 in prime_4:
        for p3 in prime_3:
            for p2 in prime_2:
                prime_sum = p2 + p3 + p4
                if prime_sum > target : break
                combinations.add(prime_sum)
    """
    print(len(combinations))


problem_87()
