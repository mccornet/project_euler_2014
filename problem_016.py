# 215 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
# What is the sum of the digits of the number 2^1000?


number = 2**1000
digitsum = 0

for digit in str(number):
    digitsum += int(digit)

print("The sum of the digits of 2^1000 is: {}".format(digitsum))

