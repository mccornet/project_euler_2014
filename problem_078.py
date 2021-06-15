import math
from array import array
'''
Let p(n) represent the number of different
ways in which n coins can be separated into piles. 
For example, five coins can separated into piles 
in exactly seven different ways, so p(5)=7.

OOOOO
OOOO O
OOO OO
OOO O O
OO OO O
OO O O O
O O O O O

Find the least value of n for which 
p(n) is divisible by one million.
'''

'''
Using the generator function

aiPn is an array to cache the values already calculated.
aiPn[0] is initialised to 1 (I got this info from another website)
aiPn[<0] = 0. Another convention not mentioned on the Mathworld page.
'''
# initialize the cache
# dictionary as fast as the list ...!
aiPn = {} #[0]*10**5
aiPn[0] = 1

def CalcPn(n):

    # P(<0) = 0 by convention
    if(n < 0): return 0
     
    # Use cached value if already calculated
    if n in aiPn : return aiPn[n]

    Pn = 0;
    for k in range(1,int(math.sqrt(n))+1): #(long k = 1; k <= n; k++)
    
        # A little bit of recursion
        n1 = n - k * (3 * k - 1) // 2;
        n2 = n - k * (3 * k + 1) // 2;

        Pn1 = CalcPn(n1);
        Pn2 = CalcPn(n2);

        # elements are alternately added and subtracted
        if(k % 2 == 1):
            Pn = Pn + Pn1 + Pn2
        else:
            Pn = Pn - Pn1 - Pn2

    #Cache calculated valued
    aiPn[n] = Pn % 10**6
    
    return Pn

n = 1
while True:
    n+=1
    test = CalcPn(n)
    if (test % 1000000 == 0):
        break

print(n)
print(test)
