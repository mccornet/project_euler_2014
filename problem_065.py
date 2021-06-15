'''
PROBLEM 65 - CONTINUED FRACTION

the sequence of the first ten convergents for √2 are:

1, 3/2, 7/5, 17/12, 41/29, 99/70, 239/169, 577/408, 1393/985, 3363/2378, ...

What is most surprising is that the important mathematical constant,

e = [2; 1,2,1, 1,4,1, 1,6,1 , ... , 1,2k,1, ...].

The first ten terms in the sequence of convergents for e are:

2, 3, 8/3, 11/4, 19/7, 87/32, 106/39, 193/71, 1264/465, 1457/536, ...
The sum of digits in the numerator of the 10th convergent is 1+4+5+7=17.

Find the sum of digits in the numerator of the 100th
convergent of the continued fraction for e.

Note:
e's a's are periodic:
2,
1, 2, 1,
1, 4, 1,
1, 6, 1,
1, 8, 1,
1, 10, 1,
1, 12, 1,

from http://en.wikipedia.org/wiki/Continued_fraction#Finite_continued_fractions

num[n]   = a[n]*num[n-1] + num[n-2]
denum[n] = a[n]*denum[n-1] + denum[n-2]

'''
# SUM DIGITS SUM DIGIT
# SUM INDIVIDUAL DIGITS 1
# using modulo, 4 times faster!
def sum_digits_1(n):
    result = 0
    while (n):
        result += (n%10)
        n //= 10
    return result

# SUM INDIVIDUAL DIGITS 2
# using string conversion
def sum_digits_2(n):
    digit_sum = 0
    for char in str(num[99]):
        digit_sum += int(char)
    return digit_sum


# store a's and num's
a   = [0]*100
num = [0]*100

# construct a's
a[0] = 2

n = 1
i = 2

while n < 99:
    # update list
    a[n]    = 1
    a[n+1]  = i
    a[n+2]  = 1
    # next i and n
    i +=2
    n +=3

# construct num's
num[0] = 2
num[1] = 3

for n in range(2,100):
    num[n] = a[n]*num[n-1] + num[n-2]

# sum the individual digits of num #100
print(sum_digits_1(num[99]))

for n in range(1,100000):
    res = sum_digits_2(num[(n%100)])


