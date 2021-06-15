'''
The nth term of the sequence of triangle numbers is given by,
tn = ½n(n+1); so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical
position and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.

If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'),
a 16K text file containing nearly two-thousand common English words,
how many are triangle words?
'''

# read file into list
with open ("problem_42.txt", "r") as myfile:
    # remove quotes arround words and split on comma
    words = myfile.read().replace('"','').split(',')

# construct array with word values
word_values = []

# for each word
for word in words:
    # reset value
    value = 0
    for char in word:
        value += ord(char)-64 #ASCII OFFSET, 'A' = 65

    word_values.append(value)

# max value
max_value = max(word_values)

# construct relevant triangle numbers
triangle_numbers = [0]

n = 1
while triangle_numbers[len(triangle_numbers)-1] < max_value:
    tn = n*(n+1)//2
    triangle_numbers.append(tn)
    n += 1

# count number of triangle_words
number_triangle_words = 0

for value in word_values:
    if value in triangle_numbers:
        number_triangle_words += 1

# print result
print("Nr of triangle words: {}".format(number_triangle_words))

