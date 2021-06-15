""" Problem 66
Consider quadratic Diophantine equations of the form:

    x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7},
we obtain the following:

    3^2 – 2×2^2 = 1
    2^2 – 3×1^2 = 1
    9^2 – 5×4^2 = 1
    5^2 – 6×2^2 = 1
    8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for
D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of
x for which the largest value of x is obtained.

PAPER: http://www.math.uchicago.edu/~may/VIGRE/VIGRE2008/REUPapers/Yang.pdf

Addition: So this equation is called pell's equation.
Finding the minimal solution is described in the paper


The paper eplains in Theorem 2.6 how from the fraction
expansion period the minimal x,y is calculated

(x1,y1) =   (pl-1; ql-1)   if l is even
            (p2l-1; q2l-1) if l is odd

NB: l: minimal period of sqrt(n)
    p,q: num,denum from quotients

So:
1.  calculate the quotients using fraction expansion
    #http://en.wikipedia.org/wiki/Methods_of_computing_square_roots

2.  Double nr of quotients when period is ODD

3.  calculate fraction x/y from quotients upto l-1 or 2l-1
    http://en.wikipedia.org/wiki/Generalized_continued_fraction

"""
from math import sqrt

def root_fraction_expansion(n):
    """ Return the quotients (a's) for the square root fraction expansion """

    #http://en.wikipedia.org/wiki/Methods_of_computing_square_roots

    if sqrt(n) == int(sqrt(n)) : return [int(sqrt(n))] # PERFECT SQUARE!

    quotients = []

    # initial values
    m_0 = 0
    d_0 = 1
    a_0 = int(sqrt(n))
    quotients.append(a_0)

    # to store a n
    a_n = a_0
    m_n = m_0
    d_n = d_0

    # The fraction should terminate when a period is detected
    a_02 = 2*a_0 # iff an = 2a0: period is detected

    while True:

        # Calculate next quotients
        m_n1 = d_n*a_n-m_n
        d_n1 = (n - m_n1**2) // d_n
        a_n1 = (a_0 + m_n1) // d_n1

        # store
        quotients.append(a_n1)

        # detect end
        if a_n1 == a_02 : return quotients

        # store results
        a_n = a_n1
        m_n = m_n1
        d_n = d_n1

def fraction_from_quotients(quotients):
    """ Returns fraction from square root continued fraction expansion quotients """

    # see: http://en.wikipedia.org/wiki/Generalized_continued_fraction
    #
    # fractions can be generated via recurrence formula
    # NB: this function may only work for square roots
    # only 'b quotients' in wiki article are used
    # 'a quotients' are 1 for roots
    #
    # num[n]   = quotients[n]*num[n-1] + num[n-2]
    # denum[n] = quotients[n]*denum[n-1] + denum[n-2]

    # first two fractions to start the recurrence
    n1 = quotients[0]
    d1 = 1

    n2 = quotients[0]*quotients[1] + 1
    d2 = quotients[1]

    # store fractions
    numerators   = [n1, n2]
    denumerators = [d1, d2]

    # numbers like 5 have a period of 1, end here!
    if len(quotients) == 1 : numerators[-1], denumerators[-1]

    # calculate the new nums and denums
    for n in range(2,len(quotients)):
        next_n = quotients[n]*numerators[n-1] + numerators[n-2]
        next_d = quotients[n]*denumerators[n-1] + denumerators[n-2]

        numerators.append(next_n)
        denumerators.append(next_d)

    return numerators[-1], denumerators[-1]

max_x = 0
max_d = 0

# find the x's
for d in range(2,1001):

    # skip perfect squares
    if sqrt(d) == int(sqrt(d)): continue

    # Step 1.
    quotients = root_fraction_expansion(d)

    # only quotients up to the repeating part (l-1)
    if len(quotients) != 2: quotients = quotients[:-1]

    # Step 2. if period is ODD,
    # double the number of quotients
    l = len(quotients) # store length to use as index
    if l & 1:
        # double the quotients
        quotients.extend(quotients)
        # double the second a0, as the repeated section starts with 2*a0
        quotients[l] *= 2

    # Step 3
    x,y = fraction_from_quotients(quotients)

    # detect new max
    if x > max_x: max_x,max_d = x,d


print("x is",max_x,"for d",max_d)







