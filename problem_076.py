'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be 
written as a sum of at least two positive integers?
'''

target = 100;

# two positive integers: 99 (+1) is max integer
integers  = [ n for n in range(1,target) ]

# storing ways in a list, use integer as index (1 ... 99)
ways = [0]*(target +1);

ways[0] = 1; # arrived at zero : no more possibilities left: 1 way possibel

# for each integer, starting from 1
for integer in integers:

    # from 1 to target, calculate ways to change
    for i in range(integer, target+1):
        ways[i] += ways[i-integer]
    #print(ways)

print("total nr of ways: {}".format(ways[-1]))