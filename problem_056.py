'''
A googol (10^100) is a massive number: 
one followed by one-hundred zeros; 
100^100 is almost unimaginably large: 
one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, 
where a, b < 100, what is the maximum digital sum?

only 100*100 possibilities, bruteforce
probably in the higher range of a and b though...
'''

#http://stackoverflow.com/questions/14939953/sum-the-digits-of-a-number-python

def sum_digits(n):
   r = 0
   while n:
       r, n = r + n % 10, n // 10
   return r

max_sum = 0;
max_ab = (0,0)

for ab in [(a,b) for a in range(1,100) for b in range(1,100)]:
    # new sum of pair
    tmp_sum = sum_digits(ab[0]**ab[1])
    # store new max if found
    if tmp_sum > max_sum: 
        max_sum = tmp_sum
        max_ab = ab

print(max_sum)
print(max_ab)