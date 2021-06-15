"""
It is easily proved that no equilateral 
triangle exists with integral length 
sides and integral area. However, the 
almost equilateral triangle 5-5-6 has 
an area of 12 square units.

We shall define an almost equilateral 
triangle to be a triangle for which 
two sides are equal and the third 
differs by no more than one unit.

Find the sum of the perimeters of all 
almost equilateral triangles with 
integral side lengths and area and whose
perimeters do not exceed one billion 
(1,000,000,000).

###############################
# Try one: Bruteforce :)
###############################

height1 = sqrt(n**2 - ((n-1)//2)**2)
height2 = sqrt(n**2 - ((n+1)//2)**2)

###############################
# Take 2:
###############################
sqrt(n**2 - ((n-1)//2)**2)
sqrt(n**2 - ((n+1)//2)**2)

->

1: n**2 - ((n-1)/2)**2 = p^2
 : 3*x^2 - 4*y^2 + 2*x -1 = 00

2: n**2 - ((n+1)/2)**2 = p^2
 : 3*x^2 - 4*y^2 - 2*x -1 = 0

solving these equations for x?

###############################
# TAKE 3:
###############################

# Sides n, n, and n+1

Define a sequence V(n) where V(1) = 5, V(2) = 65, V(3) = 901,...
V(n) = the shorter side length of the nth nearly equilateral 
Heronian triangle in Case II. V(n) satisfies a third order 
linear recursive equation:
    V(n+3) = 15V(n+2) - 15V(n+1) + V(n)


# Sides n, n+1, and n+1

Now define a sequence W(n) where W(1) = 16, W(2) = 240, 
W(3) = 3360,... W(n) = the shortest side length of the nth nearly
equilateral Heronian triangle in Case III. W(n) also satisfies
a third order linear recursive equation:
    W(n+3) = 15W(n+2) - 15W(n+1) + W(n)

http://www.had2know.com/academics/nearly-equilateral-heronian-triangles.html
http://www.had2know.com/academics/heronian-triangles-generator-calculator.html

###############################
# Pythagorian triplets
###############################

The equilateral triangle is a pythagorian triplet back to back

"""
from math import sqrt

max_side_length = 1000000000//3

# n, n, and n+1:
v = [5,65,901]
while True:
    n = len(v)
    v_n = 15*v[n-1] - 15*v[n-2] + v[n-3]
    if v_n > max_side_length : break
    v.append(v_n)


# n, n+1, and n+1:
w = [16,240,3360]   
while True:
    n = len(w)
    w_n = 15*w[n-1] - 15*w[n-2] + w[n-3]
    if w_n > (max_side_length+1) : break
    w.append(w_n)


sum_v = 0
for side in v:
    sum_v += side*3 + 1

sum_w = 0
for side in w:
    sum_w += side*3 + 2

print("Total perimeter sum: {}".format((sum_v+sum_w)))