import math
'''
If p is the perimeter of a right angle triangle with integral length sides,
{a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

p_max = 0
nr_sols_max = 0

# for each p generate possible integer triangles
# check integer triangles for being right sided.
for p in range(500,1000):

    nr_sols = 0

    #try each triangle
    for a in range (1,p//4+1):

        # b is guessed to be around some number
        b_try = p//2 - a
        b_min = b_try - 50 # no idea why 50 works :D

        for b in range(b_min,p//2 - 1):

            # triangle is now defined
            c = p - a - b

            # check if right angled
            if (a*a + b*b) == c*c:
                nr_sols += 1

    if nr_sols > nr_sols_max:
        nr_sols_max = nr_sols
        p_max = p


print("Maximized for {} with: {} solutions".format(p_max, nr_sols_max))
