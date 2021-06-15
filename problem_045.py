'''
Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:

Triangle        Tn=n(n+1)/2     1, 3, 6, 10, 15, ...
Pentagonal      Pn=n(3n−1)/2        1, 5, 12, 22, 35, ...
Hexagonal       Hn=n(2n−1)      1, 6, 15, 28, 45, ...
It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.
'''
#tn = set([n*(n+1)//2   for n in range(285,100000)])
pn = set()
hn = set()

n = 144
while not set.intersection(pn, hn):
    pn.update([n*(3*n-1)//2 for n in range(n,n+1001)]) # add a thousand new numbers
    hn.update([n*(2*n-1)    for n in range(n,n+1001)]) # add a thousand new numbers
    n+=1000

print(n)
print(set.intersection(pn, hn))


