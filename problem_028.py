import functools
# Starting with the number 1 and moving to the right
# in a clockwise direction a 5 by 5 spiral is formed as follows:
#
# 21 22 23 24 25
# 20  7  8  9 10
# 19  6  1  2 11
# 18  5  4  3 12
# 17 16 15 14 13
#
# It can be verified that the sum
# of the numbers on the diagonals is 101.
#
# What is the sum of the numbers on the diagonals
# in a 1001 by 1001 spiral formed in the same way?

# top right corner: 1,9,25,49
# n**2 for n = 1,3,5,7 .... 1001
# the other corners decrease with n-1
#
# so ring corner values diag n
# are given by
#
# SUM( n**2 - (n-1)*m ) m = 0,1,2,3

#diag_sum = 1
#for n in range(3,1002,2):
#    t1 = n**2
#    t2 = n-1
#    diag_sum += 4*t1 - 6*t2

diag_sum = 1
for n in range(3,1002,2):

    diag_sum += functools.reduce(lambda x, y: x+y, [(n**2-(n-1)*m) for m in range(0,4)])

print(diag_sum)

diag_sum = 1

for n in range(3,1002,2):

    diag_sum += sum([(n**2-(n-1)*m) for m in range(0,4)])

print(diag_sum)

diag_sum = 1
for n in range(3,1002,2):

    diag_sum += 4*n*n - 6*(n-1)

print(diag_sum)
