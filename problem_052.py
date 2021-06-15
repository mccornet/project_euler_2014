'''
It can be seen that the number, 125874,
and its double, 251748, contain exactly
the same digits, but in a different order.

Find the smallest positive integer,
x, such that 2x, 3x, 4x, 5x, and 6x,
contain the same digits.
'''

'''
1: Eerst digit moet 1 zijn,
   want vanaf 2x6 wordt het getal groter

'''

pre = 10 # to add a '1' in front
n = 1

while True:

    n += 1

    # update pre when n = pre and reset n back to 1
    # pre = 100, n = 99 -> n1 = 199
    # pre = 100, n = 100 -> pre = 1000, n = 1 -> n1 = 1001
    if (n >= pre) :
        pre *= 10
        n = 1

    n1 = n + pre
    s1 = sorted(str(n1)) # sum_digits3(n1)

    n2 = n1 * 2
    s2 = sorted(str(n2))
    if s1 != s2: continue

    n3 = n1 * 3
    s3 = sorted(str(n3))

    if s1 != s3: continue

    n4 = n1 * 4
    s4 = sorted(str(n4))
    if s1 != s4: continue

    n5 = n1 * 5
    s5 = sorted(str(n5))
    if s1 != s5: continue


    n6 = n1 * 6
    s6 = sorted(str(n6))
    if s1 != s6: continue

    # we made it!
    print("1: {}, 2: {}, 3: {}, 4: {}, 5: {}, 6: {}".format(n1,n2,n3,n4,n5,n6))

    # end
    break

