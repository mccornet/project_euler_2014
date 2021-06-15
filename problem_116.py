"""
A row of five black square tiles is to have a number 
of its tiles replaced with coloured oblong tiles 
chosen from red (length two), green (length three), 
or blue (length four).

Assuming that colours cannot be mixed there are 
7 + 3 + 2 = 12 ways of replacing the black tiles 
in a row measuring five units in length.

How many different ways can the black tiles in 
a row measuring fifty units in length be replaced 
if colours cannot be mixed and at least one 
coloured tile must be used?
"""

def binom(n,k):
    """ Returns binomial coefficients using multiplicative formula """
    # http://en.wikipedia.org/wiki/Binomial_coefficient
    res = 1
    for i in range(1,k+1):
        res *= (n-i+1)/i

    return int(round(res,0))

target_length = 50
tile_sizes = [2,3,4]

"""
As the tiles can touch each other
suppose the tile_size is 1
to achieve this, reduce target length

"""

ways = 0

"""
for tile_size in tile_sizes:

    number_tiles = 1

    while number_tiles*tile_size <= target_length:

        work_length = target_length - number_tiles*(tile_size-1)

        print("work length", work_length, "number tiles", number_tiles, "ways", binom(work_length, number_tiles) )

        ways += binom(work_length, number_tiles)

        number_tiles += 1

print(ways)
"""

for tile_size in tile_sizes:

    for number_tiles in range(1, target_length//tile_size+1):

        work_length = target_length - number_tiles*(tile_size-1)

        #print("work length", work_length, "number tiles", number_tiles, "ways", binom(work_length, number_tiles) )

        ways += binom(work_length, number_tiles)

print(ways)
