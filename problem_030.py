from functools import reduce
# Digit fifth powers
#
# Find the sum of all the numbers
# that can be written as the sum
# of fifth powers of their digits.
#
#
def is_fdp(n):

    ns = str(n)
    return n == sum([int(ns[i])**5 for i in range(0,len(ns))])

#fdp_sum = sum([n for n in range(10**6) if is_fdp(n)])

# this second version is slower
#fdp_sum = sum([n for n in range(10,10**6) if n == sum([int(str(n)[m])**5 for m in range(0,len(str(n)))])])

print(fdp_sum)


