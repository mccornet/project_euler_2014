'''
An irrational decimal fraction is created
by concatenating the positive integers:

0.1 2 3 4 5 6 7 8 9 10 11 12 13 14 15161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part,
find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

digits = ""
n = 1

while len(digits) < 1000000:
    digits += str(n)
    n += 1

prod = 1;
for d in [1, 10, 100, 1000, 10000, 100000, 1000000]:
    prod *= int(digits[d-1])

print(prod)
