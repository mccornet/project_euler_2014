"""
The rules for writing Roman numerals allow for many ways
of writing each number (see About Roman Numerals...).
However, there is always a "best" way of writing a 
particular number.

For example, the following represent all of the 
legitimate ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, 
as it uses the least number of numerals.

The 11K text file, roman.txt, contains one thousand numbers 
written in valid, but not necessarily minimal, Roman numerals;
that is, they are arranged in descending units and obey the 
subtractive pair rule.

Find the number of characters saved by writing each of these 
in their minimal form. Note: You can assume that all the Roman 
numerals in the file contain no more than four consecutive 
identical units.

######################
##### Solution 1 #####
######################

Replace and count characters spared 
(replacing is to not find IIII when counted as VIIII)

VIIII   -> IX : 3
 IIII   -> IV : 2
LXXXX   -> XC : 3
 XXXX   -> XL : 2
DCCCC   -> CM : 3
 CCCC   -> CD : 2

######################
##### Solution 2 #####
######################
findind VIIII is only saving one character
more than the 2 savings found by IIII
"""
from collections import OrderedDict

replacements = OrderedDict()
replacements["VIIII"] = "IX"
replacements["IIII"]  = "IV"
replacements["LXXXX"] = "XC"
replacements["XXXX"]  = "XL"
replacements["DCCCC"] = "CM"
replacements["CCCC"]  = "CD"

with open ("problem_89.txt", "r") as myfile:
    numerals = myfile.read()

characters_saved = 0

# 2. parse all keys
for key in replacements:

    key_occurrences =  numerals.count(key)

    # save two characters for each occurrence
    characters_saved += 2*key_occurrences

    # somethimes three
    if key in ["VIIII","LXXXX","DCCCC"]:
        characters_saved += key_occurrences

    # replace NB: RETURNS COPY :(
    numerals = numerals.replace(key,replacements[key])

print("Characters saved: ",characters_saved)



######################
#### Solution 2
######################

with open ("problem_89.txt", "r") as myfile:
    numerals = myfile.read()

keys = ["IIII","XXXX","CCCC", "VIIII","LXXXX","DCCCC"]

characters_saved = 0

for key in keys:
    key_occurrences =  numerals.count(key)

    characters_saved += key_occurrences

    if key in ["IIII","XXXX","CCCC"]:
        characters_saved += key_occurrences

print(characters_saved)