from tools import pyprimes

'''
The number 3797 has an interesting property.
Being prime itself, it is possible to continuously
remove digits from left to right,
and remain prime at each stage: 3797, 797, 97, and 7.
Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable
from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
'''
primes = pyprimes.primes()

found = 0
prime_sum = 0

prime_set = set() # if truncated number is prime,
                  # it is smaller than previous seen prime
                  # so store primes inbetween...

for _ in range(1,5):
    prime = next(primes)
    prime_set.add(prime)

while found < 11:
    prime = next(primes)
    prime_set.add(prime)

    trunc_set = set()

    # set trunc numbers equal to prime
    trunc_rl = prime
    trunc_lr = prime

    # truncate right to left
    steps = 0 # used in next part algoritm
              # is the length of the prime number
    while trunc_rl:
        steps += 1
        # integer division truncation
        trunc_rl //=10
        if trunc_rl: trunc_set.add(trunc_rl)

    # trunc from left to right
    for step in range(steps,0,-1):
        # take most left number to right using int div
        # 7856 > 7
        # multiply by 10**steps_lr
        # substract from original number
        # trunc_lr -= (trunc_lr//10**step)*10**step

        # modulo truncation
        trunc_lr = trunc_lr % 10**step

        if trunc_lr: trunc_set.add(trunc_lr)

    if trunc_set.issubset(prime_set):

        print(trunc_set)
        found += 1
        prime_sum += prime

print(prime_sum)
