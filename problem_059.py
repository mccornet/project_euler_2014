"""
Your task has been made easy, as the encryption key
consists of three lower case characters. Using cipher1.txt
a file containing the encrypted ASCII codes, and the
knowledge that the plain text must contain common English
words, decrypt the message and find the sum of the ASCII
values in the original text.
"""

import array
from itertools import permutations

with open ("problem_59.txt", "r") as myfile:
   enc_ascii = myfile.read().replace("\n","").split(",")

enc_ascii = [int(char) for char in enc_ascii]

with open ("english_words.txt", "r") as myfile:
   english_words = set(myfile.read().split("\n")[:-1])

def xor_decrypt(ascii_values, key_values):

    key_len = len(key_values)

    # GROW KEY TO ASCII SIZE
    #n = 0
    #while n < len(ascii_values) - len(key_values):
    #    key_values.append(key_values[n])
    #    n += 1

    result = []
    for i in range(len(ascii_values)):
        result.append(key_values[i % key_len] ^ ascii_values[i])

    return result

def ascii_to_str(ascii_values):

    return ''.join(chr(i) for i in ascii_values)

def generate_keys():

    for key in permutations(range(97,123), 3): yield key

    #for key1 in range(97,123):
    #    for key2 in range(97,123):
    #        for key3 in range(97,123):
    #            yield [key1,key2,key3]

key_gen = generate_keys()
n =0

def test_xor():
    test_val = [ord(char) for char in "test string"]
    test_key = [ord(char) for char in "key"]

    enc_test_val = xor_decrypt(test_val, test_key)
    enc_test_val = xor_decrypt(enc_test_val, test_key)

    print(enc_test_val)

    string_val = ascii_to_str(enc_test_val)
    words = string_val.split(" ")
    print(words)


cracked = False

decrypted_message = ''

while not cracked:
    n+=1

    # get key
    key = next(key_gen)

    # xor
    decrypted = xor_decrypt(enc_ascii, key)

    # ascii to string
    message = ascii_to_str(decrypted)

    words = message.split(' ')

    correct_words = 0

    for word in words:
        if word in english_words:
            correct_words += 1


    if correct_words > 20:
        print(key, message)
        cracked = True
        decrypted_message = message

correct_ascii_values = [ord(char) for char in decrypted_message]

total_ascii_value = sum(correct_ascii_values)

print("correct total ascii value",total_ascii_value)
