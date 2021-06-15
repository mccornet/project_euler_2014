
'''
Let r be the remainder when (a−1)n + (a+1)n is divided by a2.

For example, if a = 7 and n = 3, then r = 42: 
63 + 83 = 728 ≡ 42 mod 49. 
And as n varies, so too will r, 
but for a = 7 it turns out that rmax = 42.

For 3 ≤ a ≤ 1000, find ∑ rmax.
'''

'''
Expansion of the formula (a-1)^n + (a+1)^n mod a^2 shows that only for odd numbers
the remainder is determined by 2*a*n mod a^2
'''

r_sum_max = 0

for a in range(3,1001):
    r_max = 0
    n = 0
    while True:
        n +=1
        tmp = (a*n*2) % a**2
        if tmp > r_max:
            r_max = tmp
            continue
        
        # save
        r_sum_max += r_max
        break

print(r_sum_max)



    



