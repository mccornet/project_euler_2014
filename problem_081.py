from math import sqrt
from dijkstra import *

grid = """131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331
"""

with open ("problem_81.txt", "r") as myfile:
    grid = myfile.read()

#first step: read into numbers
# replace newline's with commas to make the split easier
# split on comma's
# remove last element which is empty (newline after last number in textfile)
# TAGS: SPLIT STRING NUMBERS
numbers = grid.replace('\n',',').split(',')[0:-1]

# http://stackoverflow.com/questions/1059559/python-strings-split-with-multiple-separators

#print(numbers)

#assume square
length = len(numbers)
side = int(sqrt(length))

#print(side)

G = dict()

for column in range(side):
    for row in range(side):

        # key is square number
        square_nr = (column + 1) + side * row

        tmp1 = dict()
        # one square right in our 1 based index

        if column < side -1 : 
            tmp1[square_nr+1]    = int(numbers[square_nr])         # square right
        
        if row < side -1    : 
            tmp1[square_nr+side] = int(numbers[square_nr+side-1])  # square lower

        # store in global
        G[square_nr] = tmp1

# add start and end
G[0] = {1:int(numbers[0])}
G[length] = {(length+1):0}

#print(G)

# calculate
l, sp = shortestPath(G, 0, (length+1))

# display
print(l)
#print(sp)
