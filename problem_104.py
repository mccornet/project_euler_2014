from decimal import Decimal as dec

LOG_PHI = dec(0.20898764024997873) 
LOG_SQRT_5 = dec(0.3494850021680094)
NINE_DIGITS = 10**9

def isPandigital(number):

	# must be divisible by 9
	# (sum of all digits should be 45)
	if number % 9 != 0 : return False

	digits = [0]*10; digits[0] = 1

	while number:
		digit = number % 10; number //= 10
		if digits[digit] : return False # early double check
		digits[digit] = 1

	if all(digits) : return True

	return False


done = False
n_fib = 2 # nth fib number
fib_1_l = 1 # keep lower nine digits
fib_2_l = 1

# while loop to calculate the next fib and check pandigital
while not done:
	n_fib += 1

	# calc last 9 digits of next fib nr
	fib_1_l, fib_2_l, = fib_2_l, (fib_2_l + fib_1_l) % NINE_DIGITS

	# first pandigital check, the last 9 digits
	if isPandigital(fib_2_l):

		# mantisse part of log(fib(n)) can be used to construct the first digits
		# see http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#fibinits
		log_fib_n = dec(n_fib*LOG_PHI - LOG_SQRT_5) % 1 # % 1: only part after comma
		fib_2_h = int(10**(log_fib_n + 8)) # NB: 10^x*10^8 = 10^(x+8), int(): only part before comma

		if isPandigital(fib_2_h):
			print(n_fib, fib_2_h, fib_2_l)
			done = True


### OLDER SOLUTIONS BELOW ###


PHI =  dec(1.61803398874989484)
SQRT_5 = dec(math.sqrt(5))
TWENTY_DIGITS = 10**20
fib_1_h = 1 # keep highest digits
fib_2_h = 1

def old_stuff():
	# while loop to calculate the next fib and check pandigital
	while not found:

		n_fib += 1

		# calc last 9 digits of next fib nr
		fib_1_l, fib_2_l, = fib_2_l, (fib_2_l + fib_1_l) % NINE_DIGITS

		""" 
		# Solution 1: Part 1
		# keep track of highest digits

		fib_1_h, fib_2_h, = fib_2_h, (fib_2_h + fib_1_h)

		# chop digits so max 20 digits stored!
		while fib_2_h > TWENTY_DIGITS:
			fib_2_h //= 10
			fib_1_h //= 10
		"""

		# first pandigital check, the last 9 digits
		if isPandigital(fib_2_l):

			""" 
			# Solution 1: Part 2
			# chop 11 digits from the highest part
			# assumes no 'leading zeros' ie: all 20 digits used
			fib_high = fib_2_h // 10**11

			if(isPandigital(fib_high)):

				print(n_fib,fib_high,fib_2_l)
				found = 1
			"""

			"""
			# Solution 2, calculate whole fib and substract the first digits
			# need whole fib nummer
			long_fib = PHI ** n_fib / SQRT_5
			
			# only first 9 digits, remove the dot via string operation
			# must also be doable via log something
			left_fib = str(long_fib) # to string
			left_fib = left_fib[0] + left_fib[2:10] # skip dot on place 1
			left_fib = int(left_fib)

			#left_fib = int(long_fib*10**8)

			# check pandigital of first 9 digits
			if(isPandigital(left_fib)):

				print(n_fib,left_fib,fib_2_l)
				found = 1
			"""
			

			""" 
			# Solution 3: calculate first nine digits directly
			# Theory: found @ http://www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/fibFormula.html#fibinits

			The whole number part of the log tells us how many 
			digits are in the number. The rest of the log of a 
			number tells us what those initial digits are. 
			This is because if the log of the number is x.y 
			then the number itself is 10^x.y = 
			10^(x+0.y) = 10^x * 10^(0.y)
			10^x is just a power of ten so it tells us how 
			to move the decimal point in 10^(0.y)


			# How to get the initial digits of fib(n):

			first_digits = 10^(log(fib(n)) - int(log(fib(n))) 

			NB: so using only part after comma of log gives first digits

			to have the first 9 digits to be in the integer part
			multiply the result by 10^8. or apply this directly:

			nine_digits = 10^(log(fib(n)) - int(log(fib(n)) + 8 )

			log(fib(n)) = log(PHI ** n / SQRT_5) = log(PHI**n) - log(SQRT_5) 
						= n*log(PHI) - log(SQRT_5)

			first_nine_digits = int(10^( log_fib_n - int(log_fib_n) + 8))

			"""

			log_fib_n = dec(n_fib*LOG_PHI - LOG_SQRT_5) % 1 # % 1, only part after comma
			first_nine_digits = int(10**(log_fib_n + 8))

			if isPandigital(first_nine_digits):
				print(n_fib, first_nine_digits, fib_2_l)
				found = 1