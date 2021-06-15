# If we list all the natural numbers below 10 that are multiples of 3 or 5,
# we get 3, 5, 6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# for loop and modulo division
summation = 0
for n in range(1,1000):
	if (n % 3 == 0 or n % 5 == 0):
		summation += n
print(summation)

# using list comprehension
numbers = [n for n in range(1,1000) if n % 3 == 0 or n % 5 == 0 ]
print(sum(numbers))

# using unions 1
print(sum(set(range(3,1000,3)).union(range(5,1000,5))))

# using unions 2
numbers = set (range(3,1000,3))
numbers |= set(range(5,1000,5))
print(sum(numbers))

# %3 or %5 = %3 AND %5 - %15
print(sum(range(3,1000,3))+sum(range(5,1000,5))-sum(range(15,1000,15)))




