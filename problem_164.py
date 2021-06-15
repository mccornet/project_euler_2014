"""
How many 20 digit numbers n (without any leading zero) 
exist such that no three consecutive digits of n have 
a sum greater than 9?
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
def p164(digits_left=20, prev1=0, prev2=0):

	# end case: no more digits left, 1 possibilty found
	if digits_left == 0: return 1

	possible = 0
	
	#if digits_left == 20 start @ 1 to prevent leading zeros
	for n in range(1 if digits_left == 20 else 0, 10 - (prev1 + prev2 ) ):

		possible+= p164(digits_left-1, n, prev1) # shift leftdigits

	return possible

print(p164())