import pyprimes

def hacked_farey(n):
    """Python function to print the nth Farey sequence, either ascending or descending."""

    a, b, c, d = 428569, 999994, 3, 7   # initial fractions

    count = 10
    while c <= n and count:
        count -= 1

        print("{}/{}".format(a,b))

        # calc k
        k = (n + b)//d

        # calc next fraction

        # next numerator: cannot be done independent!
        a, c, = c, k*c - a
        # next denumarator
        b, d = d, k*d - b

        # detect end
        #if(b == 9998 and a == 3333 or b == 999997 and a == 428570 or b == 3 and a == 1): 
            

        
        # detect end
        #if(a==1 and b == 2): break



test = hacked_farey(10**6)

print(test)