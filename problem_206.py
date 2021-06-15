"""
Find the unique positive integer whose 
square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

hk:
The square ends with a 0, so n must be a multiple of 10, 
hence n2 is a multiple of 100.
"""
from math import sqrt

a = 1020304050607080900
b = 1929394959697989990

t = 0
for n in range(int(sqrt(a))//10*10,int(sqrt(b)),10):

    square = n*n

    possible = True

    # chop two digits per iteration, check if digits match 9x 8x 7x ... 1
    # NB the first number is guaranteed to be zero.
    # cut this trailing zero to make this possible
    # 1020304050607080900
    square = square//10
    # 102030405060708090
    
    for d in range(9,0,-1):
        square = square//10
        if square%10 != d :
            possible = False
            break
        square = square//10

    if possible:
        print("unique n is",n,"square of n is",n*n)
        break






