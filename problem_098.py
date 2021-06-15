import types


# read file into list 
with open ("problem_42.txt", "r") as myfile:
    # remove quotes arround words and split on comma
    words = myfile.read().replace('"','').split(',')

words_len_sorted = [[] for _ in range(15)]

for word in words: 
    words_len_sorted[len(word)].append(word)

#print(words_len_sorted[13])

# filter palindromic words
words_letter_sorted = [{} for _ in range(15)]

anagrams = set()

for l in range(1,15):
    for word in words_len_sorted[l]:
        sorted_word = ''.join(sorted(word))
        words_letter_sorted[l][sorted_word] = word

for l in range(1,15):
    for word in words_len_sorted[l]:
        sorted_word = ''.join(sorted(word))
        if sorted_word in words_letter_sorted[l]:
            if words_letter_sorted[l][sorted_word] != word:
                anagrams.add((word, words_letter_sorted[l][sorted_word]))


print(anagrams)

