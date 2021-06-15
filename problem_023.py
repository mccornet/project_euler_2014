# Find the sum of all the positive integers 
# which cannot be written as the sum of two abundant numbers.
import divisors

def is_abundant(number):
    if divisors.proper_divisors_sum(number) > number:
        return True

    return False

# max_int
max_int = 20161

# boolean_list of positive integers
pos_integers = [False]*(max_int+1)

# construct list of the abundant nr's
abundant_nrs = [n for n in range(1,max_int+1) if is_abundant(n)]

# create all positive integers in the list
for i in range(0,len(abundant_nrs)):
    for j in range(0, len(abundant_nrs)):
        sum_ = abundant_nrs[i]+abundant_nrs[j]

        if sum_ <= max_int:
            pos_integers[sum_] = True
        else:
            break;

sum_pos_int = 0
for i in range(0,max_int+1):
    if pos_integers[i] == False:
        sum_pos_int += i

print(sum_pos_int)

