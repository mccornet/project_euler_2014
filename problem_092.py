'''
A number chain is created by continuously adding 
the square of the digits in a number to form a 
new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will 
become stuck in an endless loop. What is most 
amazing is that EVERY starting number will 
eventually arrive at 1 or 89.

How many starting numbers below ten million 
will arrive at 89?
'''

set1 = set()
set1.add(1)

set89 = set()
set89.add(89)

count89 = 0

def digit_square_sum(n):
    
    str_nr = str(n)
    square_sum = 0
    for char in str_nr:
        square_sum += int(char)**2

    return square_sum
    
# factor 3 faster!
def next_in_chain(n):
  result = 0;
  while ( n ):
    result += (n%10)*(n%10)
    n //= 10
  return result;


def number_chain(n):

    # END OF CHAIN
    if n < 600:  #only smaller results are stored
        if n in set89: return 89
        if n in set1: return 1

    # NEXT IN CHAIN
    res = number_chain(next_in_chain(n))

    if n < 600: # (9**2)*7 digits is max sum for first time
        if res == 1:
            set1.add(n)
        elif res == 89:
            set89.add(n)

    # RETURN UP THE CHAIN
    return res

for n in range(1,10**7):
    if 89 == number_chain(n):
        count89 +=1

print(count89)
    

