# If the numbers 1 to 5 are written out in words: 
# one, two, three, four, five, then there are 
# 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
# If all the numbers from 1 to 1000 (one thousand) 
# inclusive were written out in words, how many letters would be used?
#
# NOTE: Do not count spaces or hyphens. 
# For example, 342 (three hundred and forty-two) contains 23 letters 
# and 115 (one hundred and fifteen) contains 20 letters. 
# The use of "and" when writing out numbers is in compliance with British usage.

n1_9 = ["one", "two", "three", "four", "five", "six", "seven", "eigth", "nine"]
s1_9 = [len(n) for n in n1_9]

n10_19 = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
s10_19 = [len(n) for n in n10_19]

n20_90 = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
s20_90 = [len(n) for n in n20_90]

n100 = "hundred"
s100 = len(n100)

# count 1 to 9.
count_1_9 = 0;
for n in s1_9:
    count_1_9 += n
#print(count_1_9)   

# count 10 to 19
count_10_19 = 0
for n in s10_19:
    count_10_19 += n
#print(count_10_19)

# count 20 ... 99
count_20_99 = 0
for n in s20_90:
    # twenty in twenty, twentyone, twentynine
    count_20_99 += 10*n
    # add the single digits
    count_20_99 += count_1_9
#print(count_20_99)

# count sub 100
count_sub_100 = count_1_9 + count_10_19 + count_20_99
#print(count_sub_100)

# count sub 1000
count_sub_1000 = 0
# hundred from hundred (zero), hundred and one, ...., hundred and ninetynine
# for one to nine hundred
count_sub_1000 += s100*100*9

# and one, two, tree prefix
count_sub_1000 += count_1_9*100

# add sub hundred for every hundred (including 'zero hundred')
count_sub_1000 += count_sub_100*10

# add "and" for every hundred 99 subhundred
count_sub_1000 += len("and")*9*99

# count 1000
count_1000 = count_sub_1000 + len("onethousand")

print(count_1000)

input("enter to exit...")



