
for a in range(1,1000):
    for b in range(a+1,1000):

        c = 1000 - a - b

        if (a*a + b*b == c*c):
            print("{}, {}, {}".format(a,b,c))
            print("product is {}".format(a*b*c))





