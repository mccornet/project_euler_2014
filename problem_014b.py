import collections
import functools
import sys

sys.setrecursionlimit(600)

memory = [0 for n in range(10**6+1)]

def collatz_seq_length(n):

    # end of sequence
    if (n == 1): return 1

    # pre check in memory
    if n < 10**6 and memory[n] != 0 :
        return memory[n]

    # calculate the next nr in seq
    if (n & 1): # odd number
        n_new = n + (n<<1) + 1 #n = 3*n + 1
    else:
        n_new = n>>1 # n = n//2

    # calculate length
    length = 1 + collatz_seq_length(n_new)

    # store result in memory
    if n < 10**6:
        memory[n] = length

    return length

max_start = 0
max_length = 0

for i in range(1,10**6):

    l = collatz_seq_length(i)
    if l > max_length:
       max_length = l
       max_start = i

print(max_start, max_length)
