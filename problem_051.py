from tools import pyprimes
"""

By replacing the 3rd and 4th digits of 56**3 with the same
digit, this 5-digit number is the first example having seven
primes among the ten generated numbers, yielding the family:
56003, 56113, 56333, 56443, 56663, 56773, and 56993.

Consequently 56003, being the first member of this family,
is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number
(not necessarily adjacent digits) with the same digit, is part
of an eight prime value family.

Euler: "you are looking for a number for which a given block
of digits are equal. For example, in the number 12421 we could
use either *242* or 1*4*1 as our "template"."

Pythia: "you don't have to check the primes with two or four
recurring digits. If you form 8 different numbers with them,
at least once the sum of the digits (and the whole number) is
divisible by three."

# dus: zoek prime nummer met 3 dezelfde digits
# en:  laatste digit kan niet veranderd worden vanwege divisibilty test
# 8 uit 0-9 altijd bijvoorbeeld en 2 of een 5 en dus niet prime.
# start looking for smallest number from family,
# omdat 8 uit 10 mogelijkheden altijd een 0 of 1 of 2 in prime template
"""

def three_same_digits(number):
    """ returns TRUE and the digits place when 3 digits have the same value v in [0,1,2] """

    # if there is a solution we should have a hit
    # with either 3 zeros, ones or two's
    # in a 8 prime fam one of these must exist

    # store the places of the same digits in a number in list of lists
    # find smallest possibility or prime fam only
    # so cutoff at number 2.
    # after processing check for 3 same digits

    digits = [[] for _ in range(3)]
    for i in range(3) : digits[i] = []

    # filter digits from the number in loop
    number //= 10 #skip last digit
    place = 1 # index starts at 1 from the right

    while number:

        digit = number % 10 # find digit
        if digit <= 2: digits[digit].append(place)
        number //= 10 # next digit
        place += 1

    # return results
    if len(digits[0]) == 3 : return True, digits[0]
    if len(digits[1]) == 3 : return True, digits[1]
    if len(digits[2]) == 3 : return True, digits[2]

    return False, [0,0,0]

def prime_family(number, replace):
    """ yields possibile prime family members from number """

    #prime_family_list = []
    base_number = 0

    place = -1
    tmp = 0

    while number:

        # get original digit of the number
        digit = number % 10
        number //= 10

        # place index in new number
        place += 1
        tmp *= 10 # make room to add this digit if needed

        if place not in replace:
            tmp += digit

    # need to reverse the number unfortunatly
    while tmp:
        digit = tmp % 10
        tmp //= 10
        base_number *= 10
        base_number += digit

    yield base_number

    add_number = 10**replace[0] + 10**replace[1] + 10**replace[2]

    for _ in range(9):
        base_number += add_number
        yield base_number

def filter_primes(primes):

    for prime in primes:

        usable, digits = three_same_digits(prime)

        if usable:
            count = 0

            fam_gen = prime_family(prime, digits)

            for member in fam_gen:
                if member in primes: count += 1

            if count == 8 : return prime


# create list of primes from 10**5 to 10**
prime_gen = pyprimes.primes_above(10**5)
primes = [0]
while primes[-1] < 10**6 : primes.append(next(prime_gen))

# iterate over list
res = filter_primes(primes)
print(res)




