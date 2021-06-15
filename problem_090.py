from itertools import combinations

dices = list(combinations([x for x in range(10)],6))

squares = [(0,1), (0,4), (2,5), (8,1), (0,9), (1,6), (3,6), (4,9), (6,4)]

def valid_dices(d1, d2):
    for s in squares:
        if not ((s[0] in d1 and s[1] in d2) \
            or (s[1] in d1 and s[0] in d2)):
            return False

    return True
            
def extend(dice):
    if 6 in dice: 
        dice += (9,9)
    elif 9 in dice: 
        dice += (6,6)

    return tuple(set(dice))


valid_dices_c = 0
tried = set()

# TRY ALL THE COMBINATIONS!!!
for d1 in dices:

    tried.add(d1)

    for d2 in dices:

        if d2 in tried : continue # except switched dices

        d1 = extend(d1)
        d2 = extend(d2)

        if valid_dices(d1, d2): valid_dices_c += 1

print(valid_dices_c)