from itertools import product

dice_4_prob = [0]*37 # probability of rolling a sum with the dices
dice_6_prob = [0]*37

# calculate dice probabilties
# step 1, how many different ways to trow a particular number
for dice_roll in product(*[[1,2,3,4]]*9):
    dice_4_prob[sum(dice_roll)] += 1
# step 2 divide by nr of possible ways to trow the dices
dice_4_prob = [i/4**9 for i in dice_4_prob]

for dice_roll in product(*[[1,2,3,4,5,6]]*6):
    dice_6_prob[sum(dice_roll)] += 1
dice_6_prob = [i/6**6 for i in dice_6_prob]

# joint propabilty: chance every dice_4 and smaller dice_6 combination
sum_prob = 0
for i in range(len(dice_4_prob)):
    for j in range(i):
        sum_prob += dice_4_prob[i]*dice_6_prob[j]

print(sum_prob)