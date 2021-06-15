from tools import pyprimes
'''
The first two consecutive numbers to
have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

The first three consecutive numbers
to have three distinct prime factors are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

Find the first four consecutive integers
to have four distinct prime factors.
What is the first of these numbers?
'''

consecutive_count = 0
factors_db = set() # this turns out to not be of any consequence

for n in range(1,1000000,1):

    factors = list(pyprimes.factorise(n))

    if len(factors) == 4: # we met the 4 prime factor demand
        consecutive_count +=1
        # factors_db.update(factors) # list, use update!
    else:
        consecutive_count = 0 # clear conseq count
        # factors_db = set() # clear set

    # found 4 which met the first req of 4
    if consecutive_count >= 4 :
        #if len(factors_db) == 16:
        print(n-3)
        break






