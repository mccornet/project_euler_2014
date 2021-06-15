"""
Find the sum of all the numbers less than 10^8 
that are both palindromic and can be written as
the sum of consecutive squares.
"""

from math import sqrt

palindromic_consecutive_square_sums = set() # prevents doubles

TARGET = 10**8
SQRT_TARGET = int(sqrt(TARGET))

for i in range(1, SQRT_TARGET):

	consecutive_square_sum = i*i

	for j in range(i+1, SQRT_TARGET):

		consecutive_square_sum += j*j

		if consecutive_square_sum >= TARGET : break

		# quick str palindromic check
		# in java numerical check is 5 times faster
		if str(consecutive_square_sum) == str(consecutive_square_sum)[::-1]:

			palindromic_consecutive_square_sums.add(consecutive_square_sum)

print(sum(palindromic_consecutive_square_sums))
