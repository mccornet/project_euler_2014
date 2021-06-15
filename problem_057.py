import fractions
from decimal import Decimal


#http://en.wikipedia.org/wiki/Generalized_continued_fraction

A = [3,7,17]
B = [2,5,12]

for n in range(3,1001):

    An = 2*A[n-1] + A[n-2]
    A.append(An)

    Bn = 2*B[n-1] + B[n-2]
    B.append(Bn)


#print(A)
#print(B)

count = 0
for index in range(len(A)):

    if len(str(A[index])) > len(str(B[index])):
        count += 1

print(count)