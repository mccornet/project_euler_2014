"""
Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576

By concatenating each product we get the 1 to 9 pandigital,
192384576. We will call 192384576 the concatenated product of
192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by
1, 2, 3, 4, and 5, giving the pandigital, 918273645,
which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be
formed as the concatenated product of an integer with (1,2, ... , n)
where n > 1?
"""

def isPandigital(number):

    # must be divisible by 9
    # (sum of all digits should be 45)
    if number % 9 != 0 : return False

    digits = [0]*10; digits[0] = 1

    while number:
        digit = number % 10; number //= 10
        if digits[digit] : return False # early double check
        digits[digit] = 1

    if all(digits) : return True

    return False

def concatenate_numbers(*numbers):
    str_buffer = ""
    for number in numbers: str_buffer += (str(number))
    return int(str_buffer)

# try a number
upper_limit = 987654321

# 9 already results in 91 .......
# next hihger number must start with at least 92
valid_pandigitals = []

for number in range(92,9876):

    concatenated_sum = 0

    # just try (1,2, ... , n)
    # stop when new n multiplication results in a number > upper limit
    # check result for valid pandigital
    for n in range(1,10):

        tmp = concatenate_numbers(concatenated_sum, number*n)

        if tmp > upper_limit :
            break
        else:
            concatenated_sum = tmp

    if isPandigital(concatenated_sum) :
        valid_pandigitals.append(concatenated_sum)



print(max(valid_pandigitals))


