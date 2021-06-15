from problem_71 import *

"""
Consider the fraction, n/d, where n and d are positive integers.
 If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions
 for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the 
sorted set of reduced proper fractions for d ≤ 12,000?
"""

def farey_middle(a, b, e, f, m):
   """ Calculates number of fractions between a/b and e/f in F(m) using the farey sequence"""
   length = 1

   # 1, find right neighbour of a/b
   c, d = farey_right_of(a,b,m)

   # calculate new right neigbours using a faster method
   # see: http://en.wikipedia.org/wiki/Farey_sequence#Next_term
   while d != f:
      k = (m + b)//d
      b, d = d, k*d - b # no need to store b in a tmp...
      
      # update length
      length += 1

   print(length)

   return length

farey_middle(1,3,1,2,12000)
