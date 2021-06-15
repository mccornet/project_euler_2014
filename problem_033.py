from fractions import Fraction

# The fraction 49/98 is a curious fraction,
# as an inexperienced mathematician in attempting
# to simplify it may incorrectly believe that 49/98 = 4/8,
# which is correct, is obtained by cancelling the 9s.

# We shall consider fractions like,
# 30/50 = 3/5, to be trivial examples.

# There are exactly four non-trivial examples
# of this type of fraction, less than one in value,
# and containing two digits in the numerator and denominator.

# If the product of these four fractions is given
# in its lowest common terms, find the value of the denominator.

breuken = []

for i in range(10,100,10):
    for j in range(1,10):

        k = j*10
        for l in range(1,10):

            # the less than 1 in value makes 64/16 incorrect

            boven = i+j
            onder = k+l

            t1 = (i//10)/l
            t2 = boven/onder

            if (t1 == t2) and boven != onder: # strip trivial examples
                breuken.append((boven,onder))

print(breuken)

#multiply
boven = 1
onder = 1

for breuk in breuken:

    boven *= breuk[0]
    onder *= breuk[1]

print(Fraction(boven, onder))

