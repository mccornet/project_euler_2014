import math
"""
A spider, S, sits in one corner of a cuboid room, 
measuring 6 by 5 by 3, and a fly, F, sits in the 
opposite corner.  By travelling on the surfaces
of the room the shortest "straight line" distance
from S to F is 10 and the path is shown on the 
diagram.

However, there are up to three "shortest" path
candidates for any given cuboid and the shortest 
route doesn't always have integer length.

By considering all cuboid rooms with integer 
dimensions, up to a maximum size of M by M by M,
there are exactly 2060 cuboids for which the 
shortest route has integer length when M=100,
and this is the least value of M for which the 
number of solutions first exceeds two thousand; 
the number of solutions is 1975 when M=99.

Find the least value of M such that the number 
of solutions first exceeds one million.
"""

cube_set = set()

max_side = 1


nr_int_sol = 0

while nr_int_sol < 5000:

    max_side += 1
    #test = 0

    for a in range(1, max_side+1):
        for b in range(a,max_side+1):
            for c in range(b,max_side+1):

                #if (not a == max_side) and (not b == max_side) and not (c == max_side) :
                #    continue

                if (a,b,c) in cube_set:
                    continue

                cand1 = (a+b)**2 + c**2
                cand2 = (b+c)**2 + a**2
                cand3 = (c+a)**2 + b**2

                min_can = min(cand1, cand2, cand3)

                #if math.sqrt(min_can) % 1 == 0:
                if math.sqrt(min_can).is_integer():
                    nr_int_sol +=1

                cube_set.add((a,b,c))



print(max_side)
print(nr_int_sol)


