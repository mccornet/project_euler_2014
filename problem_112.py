"""
Working from left-to-right if no digit is exceeded 
by the digit to its left it is called an increasing 
number; for example, 134468.

Similarly if no digit is exceeded by the digit to 
its right it is called a decreasing number; for 
example, 66420.

We shall call a positive integer that is neither 
increasing nor decreasing a "bouncy" number; for 
example, 155349.

Clearly there cannot be any bouncy numbers below 
one-hundred, but just over half of the numbers below
one-thousand (525) are bouncy. In fact, the least 
number for which the proportion of bouncy numbers 
first reaches 50% is 538.

Surprisingly, bouncy numbers become more and more 
common and by the time we reach 21780 the proportion 
of bouncy numbers is equal to 90%.

Find the least number for which the proportion of 
bouncy numbers is exactly 99%.
"""

def is_bouncy(number):
    
    direction = 0
    d1,d2 = 0,0

    # determine direction of last two digits
    d1 = number % 10
    number = number//10

    while not direction and number:

        d2 = number % 10
        number = number//10

        if d2 > d1 : direction = 1
        if d2 < d1 : direction = 2

        d1 = d2

    # no direction, all numbers the same
    if direction == 0 or number == 0: return False

    # check if other digits dont contradict direction of last two digits
    while number:

        d2 = number % 10
        number = number//10

        if d2 > d1 and direction != 1 : return True
        if d2 < d1 and direction != 2 : return True

        d1 = d2

    return False


nr_bouncy = 0
nr_non_bouncy = 0
nr_total = 0


while (nr_non_bouncy*100) != nr_total or nr_total == 0:

    nr_total += 1

    if not is_bouncy(nr_total): nr_non_bouncy += 1



print(nr_total, nr_non_bouncy)

