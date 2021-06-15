from math import sqrt
from dijkstra import *

with open ("problem_82.txt", "r") as myfile:
    grid = myfile.read()

#first step: read into numbers
# replace newline's with commas to make the split easier
# split on comma's
# remove last element which is empty (newline after last number in textfile)
# TAGS: SPLIT STRING NUMBERS
'''
grid="""131 673 234 103 18
201 96  342 965 150
630 803 746 422 111
537 699 497 121 956
805 732 524 37  331"""
numbers = grid.split()
'''

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

        if column < side -1 : # square right
            tmp1[square_nr+1]    = int(numbers[square_nr])         
        
        if row < side -1: # square lower
            tmp1[square_nr+side] = int(numbers[square_nr+side-1])  

        if row > 0 : # square higher
            tmp1[square_nr-side] = int(numbers[square_nr-side-1])  

        # store in global
        G[square_nr] = tmp1

# add start and end
tmp1 = dict()

for s in range(0,side):
    tmp1[1+side*s] = int(numbers[side*s])
    G[side+side*s] = {length+1:0}

G[0] = tmp1


#print(G)

# calculate
l, sp = shortestPath(G, 0, (length+1))

# display
print(l)
#print(sp)
