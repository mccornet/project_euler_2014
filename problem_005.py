# 2520 is the smallest number that can be divided
# by each of the numbers from 1 to 10 without any remainder.
# What is the smallest positive number that is evenly
# divisible by all of the numbers from 1 to 20?
import time
from tools import numbthy

# http://en.wikipedia.org/wiki/Least_common_multiple#Finding_least_common_multiples_by_prime_factorization
# Here is an example:
# 48 = 2 × 2 × 2 × 2 × 3,
# 180 = 2 × 2 × 3 × 3 × 5,
# and what they share in common is two "2"s and a "3":
# Least common multiple = 2 × 2 × 2 × 2 × 3 × 3 × 5 = 720
# so the max numbers of 2 among the two numbers * max number of 3 etc


def least_common_multiple():

	numbers = [2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

	# largest prime number is max 20
	# count primenumber "list index" occurences
	prime_factors = [0] * 21

	# find prime factors of all the numbers
	for number in numbers:

		# get all the factors
		factors = numbthy.factors(number)

		print("The factors of {} are {}".format(number,factors))

		prime_factors_tmp = [0] * 21

		# count number of primenumber "list index" occurences
		if factors:

			for x in factors:

				factor = int(x)
				prime_factors_tmp[factor] += 1

			# select the highest nr of primenumber occurence of all the numbers
			for index in range(0,len(prime_factors)):
				if prime_factors_tmp[index] > prime_factors[index]:
					prime_factors[index] = prime_factors_tmp[index]

    # calculate lcm
	lcm = 1

	print("The max needed prime factors are with index starting at 0")
	print(prime_factors)

	for index in range(1,len(prime_factors)):

		lcm *= index**prime_factors[index]

	print("smallest nr: {}".format(lcm))


least_common_multiple()
