def reverse_add(number):

    str_number = str(number)
    rev_str_nr = str_number[::-1]

    return int(rev_str_nr) + number

def palindrome_check_or_reverse_add(number):

    str_number = str(number)
    rev_str_nr = str_number[::-1]

    if str_number == rev_str_nr: return 0

    return int(rev_str_nr) + number


numbers = set()

for number in range(10,10000):

    # first step, add reverse without check
    res = reverse_add(number)

    n = 1 # one iteration done without palindrome check
    while res and n < 50:
        n +=1
        # res is 0 when palindrome is detected
        res = palindrome_check_or_reverse_add(res)

    # check if palindrome not found was reason while loop stopped
    if(n == 50) : numbers.add(number)

print(len(numbers))



