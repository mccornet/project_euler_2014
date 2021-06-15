# What is the value of the first triangle number to have over five hundred divisors?

from tools import pyprimes

def triangle_nrs():

    triangle_nr = 0;
    n = 0;

    while True:
        n +=1
        triangle_nr += n;

        yield triangle_nr


nrs = triangle_nrs()

nr = 0
nr_divisors = 0

while True:

    nr = next(nrs)
    nr_divisors = 1

    factors = list(pyprimes.factorise(nr)) # list of tuples

    for tup in factors:
        nr_divisors *= (tup[1]+1)

    # print("{} heeft {} divisors".format(nr, nr_divisors))
    # input("Enter to continue")

    if nr_divisors > 500:
        break


print("{} heeft {} divisors".format(nr, nr_divisors))


