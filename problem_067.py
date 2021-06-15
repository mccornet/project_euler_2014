import math
# By starting at the top of the triangle below
# and moving to adjacent numbers on the row below,
# the maximum total from top to bottom is 23.
#
# 3
# 7 4
# 2 4 6
# 8 5 9 3
#
# That is, 3 + 7 + 4 + 9 = 23.
# calculate max path of input file

with open ("problem_67.txt", "r") as myfile:
    input_string = myfile.read()

# solution:
# solve the rows from bottom to top,
# taking the max of 2 adjacent numbers
# add this to the row above and repeat

# read into individual rows
rows = input_string.split("\n")[:-1] #fix input enter

# store maxes form previous run
maxes_cache = [0]*len(rows)

# start calculating maxes of adjacent numbers
# NB: top row as no adjacent numbers..
for row_index in range(len(rows)-1, 0, -1):

    # parse input
    numbers = [int(n) for n in rows[row_index].split()]

    # add previous maxes
    for n in range(0,len(numbers)):
        numbers[n] += maxes_cache[n]

    # allocate space for the max numbers
    maxes = [0] * (len(numbers)-1)

    # calc next maxes
    # NB: stop at [-2] as [-1] has no [-0] adjacent
    for n in range(0, (len(numbers)-1)):
        maxes[n] = max(numbers[n], numbers[n+1])

    # store result for next run
    maxes_cache = maxes

# parse top row
max_path_sum = maxes_cache[0]+int(rows[0])

print(max_path_sum)
