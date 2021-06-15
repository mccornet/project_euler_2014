from tools import pyprimes

"""
The number, 197, is called a circular prime
because all rotations of the digits:

197, 971, and 719, are themselves prime.

There are thirteen such primes below 100:

2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
"""

# to make it quicker to check if a number is a prime
# use set with all relevant primes instead of " is prime"
primes = set()

prime_gen = pyprimes.primes_below(10**6)

# fill set
for i in prime_gen: primes.add(i)


# check each prime under 10**6 for being a prime
# in for loop check all primes for the property of being circular.

def solution_1():
    # counter before the search loop.
    primes_found = 0

    for prime in primes:

        # 0. switch to string
        prime_txt = str(prime)

        # we start with the first prime rotation being valid
        valid_count = 1

        # check the rotations
        for n in range(len(prime_txt)-1):

            # first prime_txt is already valid
            # start check at the next one
            prime_txt = prime_txt[1:] + prime_txt[0]

            if int(prime_txt) in primes: valid_count += 1

        # if all rotations were valid we found a good one
        if valid_count == len(prime_txt): primes_found += 1

    print(primes_found)


def solution_2():
    # counter before loop. using set instead of manual counting
    # it turned out that using a set  with the issubset check is faster
    # than using a list and removing all valid results, to prevent double checking.

    primes_found = 0

    for prime in primes:

        # create a rotations set
        rotations = set()

        # rotate
        prime_txt = str(prime)
        for n in range(len(prime_txt)):

            rotations.add(int(prime_txt)) # add to set
            prime_txt = prime_txt[1:] + prime_txt[0] # create new number

        # if all rotations were valid we found a good one
        if rotations.issubset(primes): primes_found += 1



    print(primes_found)

def solution_3():
    # instead of counting as in solution 1,
    # check each created number using the set

    primes_found = 0

    for prime in primes: # each prime in the set.

        valid = True # assumption, proving wrong requires no count of right numbers

        # rotate using string representation of the number 123 -> "123"
        prime_txt = str(prime)
        for n in range(len(prime_txt)-1):

            prime_txt = prime_txt[1:] + prime_txt[0] # create new number

            if not int(prime_txt) in primes :

                valid = False
                break

        # if all rotations were valid we found a good one
        if valid : primes_found += 1

    print(primes_found)

solution_3()
