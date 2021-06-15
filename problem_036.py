# The decimal number, 585 = 10010010012 (binary),
# is palindromic in both bases.
# Find the sum of all numbers, less than one million, 
# which are palindromic in base 10 and base 2.
# (Please note that the palindromic number, 
# in either base, may not include leading zeros.)

# funtion taken from problem 4
def is_palindrome_dec(nr):

    # string for array based access
    str_nr = str(nr)

    # faster is to reverse a string...
    str_nr_rev = str_nr[::-1]

    if str_nr == str_nr_rev:

        return True
        
    return False


def is_palindrome_bin(nr):

    # string for array based access
    str_nr = str(bin(nr))[2:]

    # faster is to reverse a string...
    str_nr_rev = str_nr[::-1]

    if str_nr == str_nr_rev:
        return True
    return False

def is_palindrome(nr):

    # number to string
    str_dec = str(nr)

    # check if palindrome dec
    if str_dec == str_dec[::-1]:

        # check if also palindrome bin
        str_bin = str(bin(nr))[2:]  
        if str_bin == str_bin[::-1]:
            return True

    return False


def is_palindrome2(nr):

    # number to string
    str_bin = str(bin(nr))[2:]  

    # check if palindrome dec
    if str_bin == str_bin[::-1]:

        # check if also palindrome bin
        str_dec = str(nr)

        if str_dec == str_dec[::-1]:
            return True

    return False

print(sum(n for n in range(1,(10**6+1)) if is_palindrome(n)))