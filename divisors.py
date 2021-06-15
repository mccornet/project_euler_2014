import math

def proper_divisors(number):
    divisors = [1]

    # dont continue when number is 1
    if (number == 1): 
        return divisors

    # the divisors come in pairs
    # so stop the search at the square root
    r = math.floor(math.sqrt(number))

    # reduce root when square number
    # otherwise divisor will be added two times
    if r**2 == number:

        print("square number")
        divisors.append(r)
        r -= 1

    for x in range(2,r+1):

        if number % x == 0:
            divisors.append(x)
            divisors.append(number//x)

    return divisors


def proper_divisors_sum(number):
    summation = 1

    # dont continue when number is 1
    if (number == 1): 
        return summation

    # the divisors come in pairs
    # so stop the search at the square root
    r = math.floor(math.sqrt(number))

    # prevent dubble inclusion of the root 
    # when number is a square number
    # otherwise divisor will be added two times
    if r**2 == number:
        summation += r
        r -= 1

    for x in range(2,r+1):

        if number % x == 0:
            summation += x + number//x

    return summation