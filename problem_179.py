""" 179
Find the number of integers 1 < n < 10^7, for which n and n + 1 
have the same number of positive divisors. For example, 14 has 
the positive divisors 1, 2, 7, 14 while 15 has 1, 3, 5, 15.
"""
TARGET = 10**7

nr_divisors = [2]*(TARGET+1); # 1 and the number itself are two divisors
#nr_divisors[1] = 1; nr_divisors[0] = 0 # 0 and 1 are exceptions

for n in range(2, TARGET//2, 1):

	for divisor in range (n+n, TARGET+1, n):

		nr_divisors[divisor] += 1

n_1_same_nr_div = 0

for n in range(2,TARGET):

	if nr_divisors[n] == nr_divisors[n+1] : n_1_same_nr_div += 1

print(n_1_same_nr_div)
