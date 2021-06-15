'''
The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive
primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand
that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written
as the sum of the most consecutive primes?
'''
import functools
from tools import pyprimes

prime_gen = pyprimes.primes()
primes = [] # number of primes below one million

last_prime = 0

# generating al primes takes 0.5 sec
while last_prime < 10**6:
    last_prime = next(prime_gen)
    primes.append(last_prime)

# using a sliding window
min_window = 535 # @ 10**4
max_window = 547

min_prime = 9*10**5
max_prime = 10**6

found_window = 1
search_window = 0

max_index = 0
found_prime = 0

index = 0;

#for n in range(1,len(primes)):
l = len(primes)

while index + min_window < l:

    # try to expand the window from the current index position
    search_window = min_window

    summation = functools.reduce(lambda x,y : x+y, primes[index:index+search_window])

    # this is the minimum window on the current index
    if summation > max_prime: break

    # try to find a greater search window
    while search_window < max_window:

        search_window +=1

        if summation < min_prime:
            # update summation
            reduce_index = index+search_window-1
            summation += primes[reduce_index]
            continue

        if summation > max_prime:
            break

        # summation is in range...
        if summation in primes:
            # this will be our new minimum window
            min_window = search_window
            # store the prime
            found_prime = summation
            # store index
            max_index = index

        # update summation
        reduce_index = index+search_window-1
        summation += primes[reduce_index]


    # 2 update index
    index+=1

#window should be one smaller...
print(found_prime)
print(max_index)





