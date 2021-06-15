import pyprimes
import numbthy
import concurrent.futures
'''
Consider the number 15.

There are eight positive numbers less than 15
which are coprime to 15:

    1, 2, 4, 7, 8, 11, 13, 14.


The modular inverses of these numbers modulo 15 are: 

    1, 8, 4, 13, 2, 11, 7, 14

because

1*1 mod 15=1
2*8=16 mod 15=1
4*4=16 mod 15=1
7*13=91 mod 15=1
11*11=121 mod 15=1
14*14=196 mod 15=1

Let I(n) be the largest positive number m smaller
than n-1 such that the modular inverse of m modulo 
n equals m itself.

So I(15)=11.

Also I(100)=51 and I(7)=1.

Find ∑I(n) for 3≤n≤2·10^7
'''

prime_gen = pyprimes.primes()
primes = [next(prime_gen)]

mod = [0]*8

#mod[2] = set([n for n in range(10**7) if n*n%2==1])
#mod[3] = set([n for n in range(100) if n*n%3==1])

#print(mod[3])
#mod[5] = set([n for n in range(10**7) if n*n%5==1])
#mod[7] = set([n for n in range(10**7) if n*n%7==1])

print('start')


def cum_sum(a,b):

    square_mod_sum = 0

    for n in range (a,b+1):

        if pyprimes.isprime(n):

            square_mod_sum += 1

        else:
            i = n-1
            while True:
                i -= 1

                if 1 == i*i % n:

                    square_mod_sum += i

                    #print("n: {}, i: {}".format(n,i))

                    break            

    return square_mod_sum
'''
        else:
            i = n-1

            t = next(pyprimes.factorise(n))

            if False:

                print("hit!")

                while True:
                    i -= 1

                    if i in mod[t[0]]:

                        square_mod_sum += i
                        break

            else:

                while True:
                    i -= 1

                    if 1 == i*i % n:

                        square_mod_sum += i

                        break

'''
    
print(cum_sum(100000,1000000))

t = numbthy.eulerphi(15)
print(t)