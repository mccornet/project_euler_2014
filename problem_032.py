
import itertools
import functools
permutations = itertools.permutations(range(1,10)) # generator

product_sum_set = set()

for perm in permutations:

    multiplicand = perm[0]*10+perm[1] # *10+perm[2]
    multiplier   = perm[2]*100+perm[3]*10+perm[4]
    product      = perm[5]*1000+perm[6]*100+perm[7]*10+perm[8]

    if(multiplicand * multiplier == product):
        product_sum_set.add(product)

    multiplicand = perm[0] # *10+perm[2]
    multiplier   = perm[1]*1000+perm[2]*100+perm[3]*10+perm[4]
    product      = perm[5]*1000+perm[6]*100+perm[7]*10+perm[8]

    if(multiplicand * multiplier == product):
        product_sum_set.add(product)

product_sum = functools.reduce(lambda x,y : x+y, product_sum_set)


print(product_sum)