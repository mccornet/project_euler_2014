max_nr = 10**6
list_db = [0] * (max_nr+1)

collatz_length  = 0
collatz_start   = 0

def collatz_seq_length(n):
    length = 1
    cached_n = n

    while True:
        # end of sequence
        if (n == 1):
            break

        # next nr in seq
        if (n & 1): # odd number
            n += (n<<1) + 1 #n = 3*n + 1
        else:
            n = n>>1 # n = n//2

        # n allready known?
        if n < max_nr and list_db[n]:
            length += list_db[n]
            break

        # not known, length of seq +1 and next check
        length += 1

    #add to db
    list_db[cached_n] = length

    return length

for i in range(2,max_nr+1):

    l = collatz_seq_length(i)
    if l > collatz_length:
       collatz_length = l
       collatz_start = i

print(collatz_start, collatz_length)
