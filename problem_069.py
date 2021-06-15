from tools import numbthy
from tools import pyprimes
from tools import ordered_set

'''
Alternative method from project euler forum

> I just did 2*3*5*7*11*13*17,
> and got the right answer.
> The reason this works, (although you guys probably all know)
> is because multiplying in doubles will not lower phi(n).
> So you want the number with the most distinct prime factors. :)
'''

def euler_totient(n):
    ''' Euler Totient / Euler phi(n) function '''
    unique = []
    totient = n

    # needs sorted factors to work!
    for p in pyprimes.factors(n):
        if p not in unique:
            unique.append(p)
            totient -= totient//p # integer division
    return totient

def euler_totient2(n):
    ''' Euler Totient / Euler phi(n) function '''

    totient = n

    # ordered set is slower!
    factors = ordered_set.OrderedSet(pyprimes.factors(n))

    for p in factors:
        totient -= totient//p # integer division
    return totient


max_div = 0
max_n = 0

for n in range(500000,1000001):

    n_div_phi = n / euler_totient(n)

    if n_div_phi > max_div:
        max_div = n_div_phi
        max_n = n

print(max_n)
