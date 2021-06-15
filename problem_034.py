from math import factorial
from functools import reduce
# 145 is a curious number
# as 1! + 4! + 5! = 1 + 24 + 120 = 145.

# Find the sum of all numbers which are equal
# to the sum of the factorial of their digits.

#Note: as 1! = 1 and 2! = 2 are not sums they are not included.

# 999999  => 9!+9!+9!+9!+9!+9!    is 2177280 > 999999
# 9999999 => 9!+9!+9!+9!+9!+9!+9! is 2540160 < 9999999
# so max search number is somewhere between those two

sum_fac = 0


fac_table = {'1': 1, '2': 2, '3': 6, '4': 24, '5': 120, '6': 720, '7': 5040, '8': 40320,'9': 362880, '0': 1}

for number in range(10,2540160+1):

    str_num = str(number)

    tmp = sum(fac_table[str_num[i]] for i in range(len(str_num)))

    if tmp == number:
        sum_fac += tmp

print(sum_fac)

