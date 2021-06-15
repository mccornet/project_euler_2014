from math import sqrt
from decimal import *

getcontext().prec = 100

'''
It is well known that if the square root
of a natural number is not an integer, 
then it is irrational. The decimal expansion 
of such square roots is infinite without 
any repeating pattern at all.

The square root of two is 1.41421356237309504880..., 
and the digital sum of the first one 
hundred decimal digits is 475.

For the first one hundred natural numbers,
find the total of the digital sums of the 
first one hundred decimal digits for all
the irrational square roots.
'''

non_int_sqrt = []

for n in range(2,101):

    n_sqrt = sqrt(n)

    if n_sqrt != int(n_sqrt):
        non_int_sqrt.append(n)

digital_sum = 0

for n in non_int_sqrt:

    str_decimals = str(Decimal(n).sqrt())
    str_decimals = str_decimals[2:]

    for char in str_decimals:
        digital_sum += int(char)

    digital_sum += int(str_decimals[0])

    if n == 2:
        print(len(str_decimals))
        print(str_decimals)
        print(digital_sum)

print(digital_sum)



