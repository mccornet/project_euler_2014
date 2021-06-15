from tools import pyprimes
import functools
import math
# Let d(n) be defined as the sum of proper divisors of n
# (numbers less than n which divide evenly into n).
#
# If d(a) = b and d(b) = a, where a ≠ b,
# then a and b are an amicable pair
# and each of a and b are called amicable numbers.
#
# For example, the proper divisors of 220 are
# 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110;
# therefore d(220) = 284.
#
# The proper divisors of 284 are
# 1, 2, 4, 71 and 142;
# so d(284) = 220.
#
# Evaluate the sum of all the amicable numbers under 10000.

# GENERATE LIST OF PROPER DIVISORS
def proper_divisors(number):
    divisors = [1]

    # dont continue when number is 1
    if (number == 1):
        return divisors

    # the divisors come in pairs
    # so stop the search at the square root
    r = math.floor(math.sqrt(number))

    # prevent dubble inclusion of the root
    # when number is a square number
    # otherwise divisor will be added two times
    if r**2 == number:
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

max_number = 10000
sum_divisors = [0] * (max_number+1)

sum_divisors[1] = 1
sum_divisors[2] = 3

# create list of the sum of all the divisors
for number in range(1,max_number+1):

    sum_divisors[number] = proper_divisors_sum(number)

# summation of amicable numbers...
divisor_sum = 0
for index in range(1, len(sum_divisors)):

    if sum_divisors[index] < len(sum_divisors):
        # remove perfect numbers
        if index != sum_divisors[index]:
            if index == sum_divisors[sum_divisors[index]]:
                #print("{} en {}".format(str(index),str(sum_divisors[index] )))
                divisor_sum += index

print(divisor_sum)



'''
#################################
### NOT UNDERSTOOD CODE BELOW ###
###     COMPUTES DIVISORS     ###
###    USING PRIME NUMBERS    ###
#################################

    factors = LIST_OF_PRIME_FACTOR_TUPLES

    nfactors = len(factors)
    f = [0] * nfactors
    continue_var = True
    while continue_var:

        y = 1
        range_list = [factors[x][0]**f[x] for x in range(nfactors)]

        for x in range_list:
            y *= x

        if y == number :
            break

        divisors.append(y)

        i = 0
        while True:
            f[i] += 1
            if f[i] <= factors[i][1]:
                break
            f[i] = 0
            i += 1
            if i >= nfactors:
                continue_var = False

#################################
###  END NOT UNDERSTOOD CODE  ###
#################################
'''
