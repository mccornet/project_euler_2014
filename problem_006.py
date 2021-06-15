# The sum of the squares of the first ten natural numbers is,
#
# 			1^2 + 2^2 + ... + 10^2 = 385
#
# The square of the sum of the first ten natural numbers is,
#
#		(1 + 2 + ... + 10)^2 = 552 = 3025
#
# Hence the difference between the sum of the squares
# of the first ten natural numbers and
# the square of the sum is
#
#				3025 − 385 = 2640.
#
# Find the difference between
# the sum of the squares of the first
# one hundred natural numbers and the square of the sum.


numbers = range(1,101)

sum_squared_numbers = sum([number**2 for number in numbers])
squared_sum = sum(numbers)**2

difference =  squared_sum - sum_squared_numbers

print("The difference between the sum of the squares \nand the square of the sum is: {}".format(difference))



