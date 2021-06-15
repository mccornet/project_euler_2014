from itertools import product
"""
The radical of n, rad(n), is the product of distinct 
prime factors of n. For example, 504 = 23 × 32 × 7, 
so rad(504) = 2 × 3 × 7 = 42.

Let E(k) be the kth element in the sorted n column; 
for example, E(4) = 8 and E(6) = 9.

If rad(n) is sorted for 1 ≤ n ≤ 100000, find E(10000).
"""

def totient_sieve(max_number):
    """ returns list of all phis up to max_number """
    max_number += 1

    # allocate list 
    phis = [x for x in range(max_number)]

    for number in range(2,max_number):

        # number not a prime if phi modified from previous runs
        if phis[number] != number : continue

        # phi(prime) = prime-1
        phis[number] -= 1

        # update phi in all numbers containing a multiple of this prime
        for prime_multiple in range(number*2, max_number, number):
            phis[prime_multiple] = int(phis[prime_multiple] * (1-(1/number)))

    return phis

def unique_prime_factor_sieve(max_number):
    """ returns list of list of all the prime factors up to number n """
    max_number += 1

    # allocate list of empty lists
    prime_factors = [[] for _ in range(max_number)]

    # set 1 to 1
    prime_factors[1] = [1]

    for number in range(2,max_number):

        # number must be prime, so unmodified
        if prime_factors[number] != [] : continue

        # add prime to all numbers containing a multiple of this prime
        for prime_multiple in range(number, max_number, number):
            prime_factors[prime_multiple].append(number)

    return prime_factors

def prime_factor_sieve(max_number):
    """ returns list of list of all the prime factors up to number n """
    max_number += 1

    # allocate list of empty lists
    prime_factors = [[] for _ in range(max_number)]

    # set 1 to 1
    prime_factors[1] = [1]

    for number in range(2,max_number):

        # number must be prime, so unmodified
        if prime_factors[number] != [] : continue

        # for all powers of this prime and all 
        # multiples of this prime power add
        # prime to the list of the number 
        # containing this prime_power_multiple as a factor
        # p_powers(2) :2, 4, 8, 16
        # p_p_mult(2): 2, 4, 6, 8 
        # p_p_mult(4): 4, 8, 12,16
        # number 4 gets 2 from p_p_mult(2) and 2 from p_p_mult(4)
        prime_p = number
        while prime_p < max_number:
            # append all multiples of the prime powers
            for prime_p_m in range(prime_p, max_number, prime_p):
                prime_factors[prime_p_m].append(number)

            # next prime power
            prime_p *= number

    return prime_factors

def radical_sieve(max_number):
    """ returns list of all the radical values up to number n """
    max_number += 1 # all ranges stop at n-1

    # allocate list
    radicals = [1 for _ in range(max_number)]

    for number in range(2,max_number):
        # number must be prime, so unmodified
        if radicals[number] != 1 : continue

        # calculate radicals 
        for prime_multiple in range(number, max_number, number):
            radicals[prime_multiple] *= number

    return radicals

def problem_124():
    TARGET = 10**5
    E_TARGET = 10**4

    radicals = radical_sieve(TARGET)

    # create tuples of radicals
    tupled_radicals = []
    for n in range(TARGET+1):
        tupled_radicals.append((radicals[n],n))

    sorted_radicals = sorted(tupled_radicals)

    print("ANSWER: ",sorted_radicals[E_TARGET][1])

#problem_124()
