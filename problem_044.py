import math
'''
Pentagonal numbers are generated by the formula,
Pn=n(3nā1)/2. The first ten pentagonal numbers are:

    1, 5, 12, 22, 35, 51, 70, 92, 117, 145, ...

It can be seen that P4 + P7 = 22 + 70 = 92 = P8.
However, their difference, 70 ā 22 = 48, is not pentagonal.

Find the pair of pentagonal numbers, Pj and Pk,
for which their sum and difference are pentagonal
and D = |Pk ā Pj| is minimised; what is the value of D?

---
Inspecting the series shows that only the 4,7,11,14th nr can be a difference

p(j) = p(4), p(7), p(11), ....
p(k) = can be anything
'''

def pentagonal(n):
    return n*(3*n-1)//2

def is_pentagonal(n):
    return (((1 + 24 * n) ** 0.5) % 6 == 5) # someone's pentagonal test

# to find the smallest D:
# count J upwards while K downwards from J-1 to zero

# init vars for while loop
j = 1
found = False

while not found:
    j += 3 # starting at j=4, 11,
    Pj = pentagonal(j)

    for k in range(j-1,0,-1): # counting downwards from current j

        Pk = pentagonal(k)

        if is_pentagonal(Pj-Pk) and is_pentagonal(Pj+Pk):

            print("j is: {}, k is: {}, |k-j| is: {}".format(Pj,Pk,Pj-Pk))

            found = True # exit the while loop
            break # exit for loop
