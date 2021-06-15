import collections
import functools

"""
A bag contains one red disc and one blue disc. 
In a game of chance a player takes a disc at random 
and its colour is noted. After each turn the disc is 
returned to the bag, an extra red disc is added, and 
another disc is taken at random.

The player pays £1 to play and wins if they have taken
 more blue discs than red discs at the end of the game.

If the game is played for four turns, the probability 
of a player winning is exactly 11/120, and so the maximum
prize fund the banker should allocate for winning in this 
game would be £10 before they would expect to incur a loss.
Note that any payout will be a whole number of pounds and 
also includes the original £1 paid to play the game, so 
in the example given the player actually wins £9.

Find the maximum prize fund that should be allocated
to a single game in which fifteen turns are played.
"""

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
def rec_play(nr_rounds, round_nr=1, blue_nr=0):

    #print("round:", round_nr, "blue", blue_nr)

    total, wins = 0, 0

    # +1: nr_rounds of play realised when round_nr in call is nr_rounds+1
    if round_nr == nr_rounds+1: 
        if blue_nr > nr_rounds/2 : # did we win?
            return 1,1
        else:
            return 1,0

    # take a disc

    # we can take a blue disc only once:
    t_b, w_b = rec_play(nr_rounds, round_nr+1, blue_nr+1, )

    # we can take a red disc
    t_r, w_r = rec_play(nr_rounds, round_nr+1, blue_nr)

    t_r *= round_nr # we can do that the number of red discs in the bag
    w_r *= round_nr

    total += t_r + t_b
    wins += w_r + w_b

    return total,wins

t, w = rec_play(15)

print(t//w)