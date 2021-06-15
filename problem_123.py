import pyprimes
'''
Let pn be the nth prime: 2, 3, 5, 7, 11, ..., 
and let r be the remainder when (pn−1)n + (pn+1)n is divided by pn2.

For example, when n = 3, p3 = 5, and 43 + 63 = 280 ≡ 5 mod 25.

The least value of n for which the remainder first exceeds 10**9 is 7037.

Find the least value of n for which the remainder first exceeds 10**10.
'''

'''
Expansion of the formula (pn-1)^n + (pn+1)^n shows that only for odd numbers
the remainder is determined by 2*n*pn mod pn^2
'''

test_p = pyprimes.nth_prime(7037)

print( test_p)

result = 2*7037*test_p % test_p**2

print( result)

prime_stream = pyprimes.primes()

for n in range(7033): next(prime_stream)

n = 7033

while True:

    pn =  next(prime_stream)
    pn =  next(prime_stream)
    n  += 2

    if 2*pn*n > 10**10:
        break

print(n)
print(pn)




