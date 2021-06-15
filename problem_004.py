# A palindromic number reads the same both ways.
# The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(nr):

	# string for array based access
	str_nr = str(nr)
	length = len(str_nr)
	half   = int(length/2)

	# assume the number is a palindrome
	# return false when prove otherwise is found
	for index in range(0, half):

		#first = index
		#second = length -1 -index
		#print("The first index is: {} the second index is: {} \n".format(first, second))

		if (str_nr[index] != str_nr[length-1-index]):
			return False;

	return True

product = 0

# two numbers, from 100 to 999
for i in range(100,1000):
	for j in range(100,1000):

		# calc product
		tmp_product = i * j;

		# check if  bigger and palindrome
		if tmp_product > product and is_palindrome(tmp_product):

			product = tmp_product;


print("The largest palindrome is: {}".format(product))

