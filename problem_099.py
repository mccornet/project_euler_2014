"""   problem 99
find the biggest exponent pair in the file problem99.txt

a^b is identical to base^(b * logbase a)
find biggest result of b * log10 a
"""

from math import log10, exp, log

with open ("problem_99.txt", "r") as myfile:
   power_pairs = myfile.read().split("\n")

max_value = 0
max_line = 0
line_nr = 0
max_line_nr = 0

for power_pair in power_pairs:
    line_nr += 1

    numbers = power_pair.split(",")
    res = int(numbers[1])*log(int(numbers[0]))

    if res > max_value:
        max_value = res
        max_line_nr = line_nr

print("max value on line:",max_line_nr)
