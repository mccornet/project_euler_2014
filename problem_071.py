"""
Consider the fraction, n/d, where n and d are positive integers.
 If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8
in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2,
 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000
in ascending order of size, find the numerator of the fraction
immediately to the left of 3/7.
"""

# http://en.wikipedia.org/wiki/Farey_sequence
# http://arxiv.org/pdf/0801.1981.pdf [1]

# Iterative Algorithm (xgcd)
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def iterative_egcd(a, b):
    x,y, u,v = 0,1, 1,0
    while a != 0:
        q,r = b//a,b%a; m,n = x-u*q,y-v*q # use x//y for floor "floor division"
        b,a, x,y, u,v = a,r, u,v, m,n
    return b, x, y

# Modular inverse
# https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def modinv(a, m):
    g, x, y = iterative_egcd(a, m)
    if g != 1:
        return None
    else:
        return x % m


def farey_left_of(a, b, m):
	""" calculates left neighbour of fraction a/b in the farey sequence F(m) """

	# "any x0 such that b * x0 = -1 mod a" [1]
	# https://en.wikipedia.org/wiki/Multiplicative_modular_inverse
	x_0 = -1* modinv(b,a)

	t = (a*m - b*x_0 -1)//(a*b)

	a_1 = a*t + x_0
	b_1 = b*t + (b*x_0+1)//a

	print("{} / {}".format(a_1, b_1))
	return a_1, b_1

	# y_0 an integer such that a*y_0 = 1 mod(b) [1]

	#y_0 = modinv(a,b)
	#t = ((m-y_0)//b)
	#a_1 = a*t + (a*y_0-1)//b
	#b_1 = b*t + y_0

	#print("{} / {}".format(a_1, b_1))

def farey_right_of(a, b, m):
	""" calculates right neighbour of fraction a/b in the farey sequence F(m) """

	# see [1] for more info
	x_0 = modinv(b,a)

	t = (a*m - b*x_0 +1)//(a*b)

	a_1 = a*t + x_0
	b_1 = b*t + (b*x_0-1)//a

	print("{} / {}".format(a_1, b_1))
	return a_1, b_1

	#y_0 = -1 * modinv(a,b)
	#t = ((m-y_0)//b)
	#a_1 = a*t + (a*y_0+1)//b
	#b_1 = b*t + y_0

	#print("{} / {}".format(a_1, b_1))


a,b = farey_left_of(3,7,10**6)
