from tools import pyprimes

def euler_form(a,b):
    n = -1
    while True:
        n += 1
        yield int(n**2 + a*n + b)


max_cons_primes = 0
coeff_a = 0
coeff_b = 0

# b can only be a prime number
# n = 0 => 0**2 + 0*a + b = b
primes = pyprimes.primes()
b_primes = []
while True:
    next_prim = next(primes)
    if next_prim > 1000:
        break
    b_primes.append(next_prim)

# a has to be odd, except when b = 2
# all primes except 2 are odd, so
# n = 1 => odd + ... + odd = odd
# odd + odd = even, n*a must be odd,
# only possible with odd a

# for safety we should consider b = 2 with even a...
# but lets try the non b=2 solutions first
for a in range(-999,1000,2):
    for b in b_primes:

        # rest consecutive primes
        cons_prim = 0

        # init generator
        func = euler_form(a,b)

        while pyprimes.isprime(next(func)):
            cons_prim += 1

        if cons_prim > max_cons_primes:
            coeff_a = a
            coeff_b = b
            max_cons_primes = cons_prim

print(coeff_a*coeff_b)

