"""
By counting carefully it can be seen that a rectangular
grid measuring 3 by 2 contains eighteen rectangles:


Although there exists no rectangular grid that contains 
exactly two million rectangles, find the area of the grid 
with the nearest solution.
"""

subgrids = []

for a in range(1,10000):
    for b in range(1,1000):

        # the number of subgrids is given by
        # a*(a+1)*b*(b+1)//4
        res = abs(a*(a+1)*b*(b+1)//4 - 2*10**6)

        subgrids.append((a,b,res))

#print(results)

found = subgrids[0]


for res in subgrids:
    if subgrids[2] < found[2]:
        found = res

print(found)
