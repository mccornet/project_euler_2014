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
def rec_solve(length, min_tile_length, black=False):

    # simplest case, everything filled in gives one possible way
    if length == 0 : return 1

    res = 0

    # fill in all possible tile sizes
    for tile in range(min_tile_length,length+1):

        # the tile does not touch a side? one black tile between the next tiles
        if length - tile != 0:
            res += rec_solve(length-(tile+1), min_tile_length)
        else:
            res += 1 # rec_solve(0) returns 1 in this case

    # instead of tile: fill in a nr of black squares 
    # only if previous tile was not black
    if black == False:
        for empty in range(1,length+1):
           res += rec_solve(length - empty, min_tile_length, True)

    return res

res = 0
n = 50

while res < 10**6:
    n += 1
    res = rec_solve(n, 50)


print(n)