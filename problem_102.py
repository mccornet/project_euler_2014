""" Problem 102

In triangles.txt, a 27K text file containing the 
co-ordinates of one thousand "random" triangles, 
find the number of triangles for which the interior 
contains the origin.

# Method 1:

A triangle contains the origin when 
1) point p is on same side as point c from the line ab
2) point p is on same side as point b from the line ac
3) point p is on same side as point a from the line cb

this can be determined via the direction of the crossproduct
check a_b x a_c same direction as a_b x a_p etc

source: http://www.blackpawn.com/texts/pointinpoly/

# Method 2: slightly faster :)
Barycentric Technique

# method 3: from proj euler forum:
"Let's suposse that we have a triangle ABC , and the origin is O(0, 0)
If O in the interior of the triangles, we should have:

Area(ABC) = Area(OAB) + Area(OBC) + Area(OAC)

def calcTriangArea(xA, yA, xB, yB, xC, yC):
    return 1 / 2.0 * abs(xA * (yB - yC) + xB * (yC - yA) + xC * (yA - yB))

"""
from math import sqrt

def dotproduct(a,b):
    """ calc dot product of vectors a and b in 2 dim plane """
    return a[0]*b[0]+a[1]*b[1]

def crossproduct(a,b):
    """ calc cross product of vectors a and b in 2 dim plane """
    return a[0]*b[1]-a[1]*b[0]

def vertex_to_vector(p1,p2):
    """ calc vector from two points """
    a = p2[0] - p1[0]
    b = p2[1] - p1[1]

    return (a,b)

def point_in_triangle_1(a,b,c,p):
    """ determine if point p in triangle with a,b,c via crossproduct """

    a_b = vertex_to_vector(b,a)
    a_c = vertex_to_vector(c,a)
    b_c = vertex_to_vector(c,b)
    c_a = vertex_to_vector(a,c)
    c_b = vertex_to_vector(b,c)

    a_p = vertex_to_vector(p,a)
    b_p = vertex_to_vector(p,b)
    c_p = vertex_to_vector(p,c)

    # direction the same, both pos or neg
    # res only neg when one neg

    # c side from line a-b
    ab_x_ap = crossproduct(a_b,a_p)
    ab_x_ac = crossproduct(a_b,a_c)
    if ab_x_ap * ab_x_ac < 0: return False

    # b side from line a-c
    ac_x_ap = crossproduct(a_c,a_p)
    ac_x_ab = crossproduct(a_c,a_b)
    if ac_x_ap * ac_x_ab < 0: return False

    # a side from line b-c
    cb_x_cp = crossproduct(c_b,c_p)
    cb_x_ca = crossproduct(c_b,c_a)
    if cb_x_cp * cb_x_ca < 0: return False

    return True

def point_in_triangle_2(a,b,c,p):
    """ determine if point p in triangle with a,b,c via projection """
    # adopted from http://www.blackpawn.com/texts/pointinpoly/

    # compute vectors
    a_p = vertex_to_vector(p,a)  
    a_b = vertex_to_vector(b,a)
    a_c = vertex_to_vector(c,a)

    # Compute dot products
    dot00 = dotproduct(a_c, a_c)
    dot01 = dotproduct(a_c, a_b)
    dot02 = dotproduct(a_c, a_p)
    dot11 = dotproduct(a_b, a_b)
    dot12 = dotproduct(a_b, a_p)

    # Compute barycentric coordinates
    invDenom = 1 / (dot00 * dot11 - dot01 * dot01)
    u = (dot11 * dot02 - dot01 * dot12) * invDenom
    v = (dot00 * dot12 - dot01 * dot02) * invDenom

    # Check if point is in triangle
    return (u >= 0) and (v >= 0) and (u + v < 1)


with open ("problem_102.txt", "r") as myfile:
   triangle_lines = myfile.read().split("\n")[:-1]

origin_count = 0

for triangle_line in triangle_lines:

    # extract points from string
    points = triangle_line.split(",")
    points = [int(s) for s in points]

    a = (points[0],points[1])
    b = (points[2],points[3])
    c = (points[4],points[5])
    p = (0,0)

    if point_in_triangle_1(a,b,c,p):
        origin_count += 1

print("number of triangles containing the origin:",origin_count)