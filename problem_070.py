"""
Find the value of n, 1 < n < 10^7, for which φ(n)
is a permutation of n and the ratio n/φ(n)
produces a minimum.
"""
from problem_072 import phi_sieve_1

phis = phi_sieve_1(10**7)

def is_permutation(num1, num2):
    digits = [0]*10

    while num1:
        digits[(num1%10)] +=1
        num1 = num1 // 10

    while num2:
        digits[(num2%10)] -=1
        num2 = num2 // 10

    if digits == [0]*10: return True
    return False

def find_permutations(phis):
    res = dict()

    for index,phi in enumerate(phis):
        if(phi == index-1) : continue # skip primes
        if(phi == 0) : continue # skip zero

        if is_permutation(index,phi):
            res[index] = index/phi

    return res

valid_sols = find_permutations(phis)

def filter_valid_sol(solutions):

    n = 0
    n_div_phi_n = 100

    for key,val in solutions.items():
        if val < n_div_phi_n:
            n = key
            n_div_phi_n = val

    print("max n/phi(n) for n:",n, n_div_phi_n)

filter_valid_sol(valid_sols)
