"""
It turns out that 12 cm is the smallest length of wire 
that can be bent to form an integer sided right angle 
triangle in exactly one way, but there are many more examples.

	12 cm: (3,4,5)
	24 cm: (6,8,10)
	30 cm: (5,12,13)
	36 cm: (9,12,15)
	40 cm: (8,15,17)
	48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent
to form an integer sided right angle triangle, and other 
lengths allow more than one solution to be found; for example,
using 120 cm it is possible to form exactly three different
integer sided right angle triangles.

	120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values
of L ≤ 1,500,000 can exactly one integer sided right angle 
triangle be formed?
"""
from numpy import matrix,array

def prim_pyth_triplet(max=None):
	''' generate all primative triples with  perimeter <= max '''
	# depends on numpy: matrix,array

	# http://mathworld.wolfram.com/PythagoreanTriple.html
	# NB: row-vector * matrix = matrix-transposed * column-vector
	# http://en.wikipedia.org/wiki/Formulas_for_generating_Pythagorean_triples
	#
	# from one primitive triplet three new primitive triplets can be generated via matrix multiplication
	# (a1,b1,c1) = u*(a,b,c)
	# (a2,b2,c2) = a*(a,b,c)
	# (a3,b3,c3) = d*(a,b,c)

	u = matrix( [[1,2,2], [-2,-1,-2], [2,2,3]] )
	a = matrix( [[1,2,2], [2,1,2], [2,2,3]] )
	d = matrix( [[-1,-2,-2], [2,1,2], [2,2,3]] )
	
	# first pythagorian triplet
	triplets = [ array([3,4,5]) ]

	while triplets:
		# yield perimeter current triplets
		# for i in triplets: yield i

		''' For PE 75: yield the perimeters '''
		for i in triplets: 
			yield sum(i)

		# calculate new triplets by multiplying all triplets with u, d and a
		g=( (triplet*matrix).getA1() for triplet in triplets for matrix in (u,a,d) )

		# store new valid triplets in triplets list
		triplets = [ i for i in g if max is None or sum(i)<=max ]

MAX_PERI = 1500000

# perimeter generator function
peri_gen = prim_pyth_triplet(MAX_PERI)

# generate list of all primitive perimeters
primitive_perimeters = []
for p in peri_gen: primitive_perimeters.append(p)

# calculate all multiples of primitive perimeters
perimeters = [0]*(MAX_PERI+1) # 'mask' where perimeter is index
for p in primitive_perimeters:
	multiple_p = p # start @ multiple 1
	while multiple_p <= MAX_PERI:
		perimeters[multiple_p] += 1 # mask peri
		multiple_p += p # multiple 2, 3, ...

# count number of perimeters possible from only one prim triplet
uniq = 0
for p in perimeters:
	if p == 1: uniq += 1

# print result
print("Number of unique perimeters: {}".format(uniq))