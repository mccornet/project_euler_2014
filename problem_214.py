from problem_124 import totient_sieve

def problem_412():
    totients = totient_sieve(40*10**6)

    print("calculated totiens")

    valid_chains = []

    TARGET_CHAIN_LENGTH = 25
    TARGET_CHAIN_LENGTH_1 = TARGET_CHAIN_LENGTH+1

    chain_lengths = dict()
    chain_lengths[1] = 1
    chain_lengths[2] = 2
    chain_lengths[4] = 3
    
    for n in range(1,40*10**6+1):
        
        # only check primes
        if totients[n] != n-1 : continue

        chain = 0
        p = n

        while chain <= TARGET_CHAIN_LENGTH_1:

            if p == 1:
                chain += 1
                break
            else:
                chain += 1
                p = totients[p]

        if chain == TARGET_CHAIN_LENGTH:
            valid_chains.append(n)

    print(sum(valid_chains))

problem_412()