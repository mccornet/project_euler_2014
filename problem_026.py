def recurring_length(n):

    # result = [0]
    remainder = 1
    index = 1
    remainders = {1:1}

    while True:

        index += 1

        res = int((remainder*10)/n)
        remainder = (remainder*10)%n

        # save result, but not needed
        # result.append(res)

        # check for repeat
        if remainder in remainders: break

        # check for break
        if remainder == 0 : return 0

        # save remainder
        remainders[remainder] = index

    # return length of  the recurring sequence
    return index - remainders.get(remainder)


longest_rec = 0
longest_d = 0

for d in range(3,1000):

    length = recurring_length(d)

    if length > longest_rec:
        longest_rec = length
        longest_d = d

print(longest_d)
