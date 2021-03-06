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

max_side = 1

target = 10**6
nr_int_sol = 0

while nr_int_sol < target:

    max_side += 1

    #for a in range(max_side, max_side+1):
    #    for b in range(1,max_side+1):
    #        for c in range(b,max_side+1):

    #for a in range(max_side, max_side+1):
    for bc in range(3,max_side*2+1):
            #for c in range(b,max_side+1):
             
        # if c<b<a!
        min_can = bc*bc + max_side*max_side

        if math.sqrt(min_can).is_integer():
        
            if bc <= max_side :
                nr_int_sol += bc // 2
            else:
                # c<b<a!
                nr_int_sol += 1 + (max_side - (bc+1)//2)

print(max_side)
print(nr_int_sol)


