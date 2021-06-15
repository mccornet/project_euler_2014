"""
Consider the number 45656. 
It can be seen that each pair of consecutive digits of 45656 has a difference of one.
A number for which every pair of consecutive digits has a difference of one is called a step number.
A pandigital number contains every decimal digit from 0 to 9 at least once.
How many pandigital step numbers less than 1040 are there?
"""
import collections
import functools
class memoized(object):
   '''Decorator. Caches a function's return value each time it is called.
   If called later with the same arguments, the cached value is returned
   (not reevaluated).
   '''
   def __init__(self, func):
      self.func = func
      self.cache = {}
   def __call__(self, *args):
      if not isinstance(args, collections.Hashable):
         # uncacheable. a list, for instance.
         # better to not cache than blow up.
         return self.func(*args)
      if args in self.cache:
         return self.cache[args]
      else:
         value = self.func(*args)
         self.cache[args] = value
         return value
   def __repr__(self):
      '''Return the function's docstring.'''
      return self.func.__doc__
   def __get__(self, obj, objtype):
      '''Support instance methods.'''
      return functools.partial(self.__call__, obj)

@memoized
def p178(digits_left = 40, digit_count=tuple([0]*10), last_digit=0, started=False):

	# end case: no more digits left
	if digits_left == 0:	
		if all(digit_count) : return 1 # check if pandigital
		return 0

	possible = 0

	# number not 'started':
	# choose all kind of digits, but dont count zero for pandigital
	if not started:

		for n in range(0,10):

			tmp = list(digit_count) # modifiable copy
			if n > 0: 
				tmp[n] = 1  # mark digit used
				started = 1

			possible += p178(digits_left-1,tuple(tmp),n,started)

	else:
		# number started, follow the one higher or one lower rule
		next_digits = [last_digit+1, last_digit-1]

		for n in next_digits:

			if not (0 <= n <= 9) : continue

			tmp = list(digit_count); tmp[n] = 1 # copy and mark digit as used

			possible += p178(digits_left-1,tuple(tmp),n,True)

	return possible

print(p178())