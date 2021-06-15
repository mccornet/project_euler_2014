"""
The first ten continued fraction representations 
of (irrational) square roots are:

√2 = [1;(2)], period=1
√3 = [1;(1,2)], period=2
√5 = [2;(4)], period=1
√6 = [2;(2,4)], period=2
√7 = [2;(1,1,1,4)], period=4
√8 = [2;(1,4)], period=2
√10= [3;(6)], period=1
√11= [3;(3,6)], period=2
√12= [3;(2,6)], period=2
√13= [3;(1,1,1,1,6)], period=5

Exactly four continued fractions, for N ≤ 13, have an odd period.

How many continued fractions for N ≤ 10000 have an odd period?
"""

from math import sqrt

#http://en.wikipedia.org/wiki/Methods_of_computing_square_roots
# UPDATED AND REUSED IN PROBLEM 66
def continued_fraction_period(n):
    """ Returns period of the continued fraction expansion """

    if sqrt(n) == int(sqrt(n)) : return 0 # PERFECT SQUARE!

    # initial values 
    m_0 = 0
    d_0 = 1
    a_0 = int(sqrt(n))

    # to store a n
    a_n = a_0
    m_n = m_0
    d_n = d_0

    # loop variables
    digit_nr = 0 # period counter
    a_02 = 2*a_0 # iff an = 2a0 period detected

    while True:

        digit_nr += 1

        m_n1 = d_n*a_n-m_n
        d_n1 = (n - m_n1**2) // d_n
        a_n1 = (a_0 + m_n1) // d_n1

        # detect end and period
        if a_n1 == a_02 : return digit_nr

        # store results
        a_n = a_n1
        m_n = m_n1
        d_n = d_n1

counter = 0

for N in range(1,10001):

    res = continued_fraction_period(N)
    if res & 0x1 :
        counter += 1

print(counter)