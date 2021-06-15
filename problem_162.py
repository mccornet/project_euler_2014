"""
How many hexadecimal numbers containing at most sixteen hexadecimal 
digits exist with all of the digits 0,1, and A present at least once?
Give your answer as a hexadecimal number.
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
def p162(digits_left=16, digits_used=tuple([0]*11), started=0):
	""" digits left, digits used counter, 'started' used to prevent counting the leading zero """

	# end case 1, no more digits left
	if digits_left == 0: 
		if sum(digits_used) == 3: return 1 # only 0, 1, and A are marked
		return 0

	possible = 0

	# try ALL the digits
	for n in range(0,16):

		tmp = list(digits_used) # modifiable copy

		if n == 10 or n == 1 or n == 0: tmp[n] = 1 # mark 0,1,A 
		if started == 0 and n == 0: tmp[0] = 0     # dont count leading zeros, overwites prev statement
		if n : started = 1 # only overwrite started when n is pos

		possible += p162(digits_left-1, tuple(tmp), started)

	return possible

print(str(hex(p162())).upper()[2:])