""" Problem 100

If a box contains twenty-one coloured discs, 
composed of fifteen blue discs and six red discs,
and two discs were taken at random, it can be 
seen that the probability of taking two blue discs,
P(BB) = (15/21)×(14/20) = 1/2.

The next such arrangement, for which there is 
exactly 50% chance of taking two blue discs at 
random, is a box containing eighty-five blue 
discs and thirty-five red discs.

By finding the first arrangement to contain 
over 10^12 = 1,000,000,000,000 discs in total, 
determine the number of blue discs that the 
box would contain.

a/b * (a-1)/(b-1) = 1/2

a(a-1)   1
------ = -
b(b-1)   2

giving the following diophantic quadratic equation
2 a^2 - 2a -b^2 + b = 0

NB: solving via Quadratic_formula turned out impossible
http://en.wikipedia.org/wiki/Quadratic_equation#Quadratic_formula

    1 + sqrt(1 + 2(b^2-b))
a = ----------------------
             2

http://www.wolframalpha.com/input/?
i=x+%3D+%281+%2B+sqrt%281%2B2*%28y%5E2-y%29%29%29%2F2+%2C+y%3D21

calculating possible a's from b's 
and checking perfect square: impossible
"""
from math import sqrt


P =  3
Q =  2
K = -2
R =  4
S =  3
L = -3

x = [0,1]
y = [1,1]

i = 1
while y[-1] < 10**12:

    Xn_1 = P*x[i] + Q*y[i] + K
    Yn_1 = R*x[i] + S*y[i] + L

    x.append(Xn_1)
    y.append(Yn_1)
    
    print(x[-1],y[-1])

    i += 1

print(x[-1],y[-1])