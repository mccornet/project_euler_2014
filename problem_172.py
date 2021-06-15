""" 
How many 18-digit numbers n (without leading zeros) are 
there such that no digit occurs more than three times in n?
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
def p172(digits_left=18, digit_count=tuple([0]*10)):

	# end case, no more digits left
	if digits_left == 0: return 1

	possible = 0

	# try ALL THE DIGITS!
	# start with min 1 at first digit to prevent leading zeros
	for n in range(1 if digits_left==18 else 0, 10): 

		if digit_count[n] == 3 : continue # skip used up digits

		# make modifiable copy and mark digit as used +1
		tmp = list(digit_count)
		tmp[n] += 1

		possible += p172(digits_left-1, tuple(tmp))

	return possible

print(p172())

