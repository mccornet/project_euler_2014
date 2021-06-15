import pyprimes
'''
It is possible to write ten as the sum of primes 
in exactly five different ways:

7 + 3
5 + 5
5 + 3 + 2
3 + 3 + 2 + 2
2 + 2 + 2 + 2 + 2

What is the first value which can be written 
as the sum of primes in over five thousand different ways?
'''
prime_gen = pyprimes.primes()
primes  = [next(prime_gen)]

ways = [0]
target= 10

while ways[-1] < 5000:

    target += 1;

    # generate primes up to target
    while primes[-1] < target : primes.append(next(prime_gen))

    # storing ways in a list, use integer as index (1 ... 99)
    ways = [0]*(target +1);

    ways[0] = 1; # arrived at zero : no more extra possibilities left: 1 way possible

    # for each integer, starting from 1
    # last prime is bigger than target!
    for prime in primes[0:-1]:

        # from 1 to target, calculate ways to change
        for i in range(prime, target+1):
            ways[i] += ways[i-prime]
        #print(ways)

print("{} can be written as the sum of primes in {} ways".format(target,ways[-1]))