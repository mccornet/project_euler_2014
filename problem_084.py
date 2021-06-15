from random import *
from collections import Counter
from collections import deque
""" Monopoly Odds - Project Euler 84

The heart of this problem concerns the likelihood of visiting a particular square.
That is, the probability of finishing at that square after a roll. 
For this reason it should be clear that, with the exception of G2J 
for which the probability of finishing on it is zero, the CH squares
will have the lowest probabilities, as 5/8 request a movement to 
another square, and it is the final square that the player finishes 
at on each roll that we are interested in. We shall make no distinction
between "Just Visiting" and being sent to JAIL, and we shall also ignore
the rule about requiring a double to "get out of jail", assuming
that they pay to get out on their next turn.

By starting at GO and numbering the squares sequentially from 00 to 39
we can concatenate these two-digit numbers to produce strings that correspond
with sets of squares.

Statistically it can be shown that the three most popular squares, in order, 
are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00. 

So these three most popular squares can be listed with the six-digit modal string: 102400.

If, instead of using two 6-sided dice, two 4-sided dice are used, find the six-digit modal string.
"""


chance_cards = []
community_chest_cards = []
square_hit_counter = dict() 
position = 0 # start at 'go'

# init random seed
seed()

# init square hit counter
for square in range(40): square_hit_counter[square] = 0

# construct community chest cards
community_chest_cards = [0, 10]
for n in range(14): community_chest_cards.append("nop")

# construct chance cards
chance_cards = [0,10,11,24,39,5,"next_r", "next_r", "next_u", "back_3", "nop", "nop", "nop", "nop", "nop", "nop"]

# shuffle cards
#shuffle(chance_cards)
#shuffle(community_chest_cards)

def chance(position):
	""" Returns new position based on chance card in stack """
	# pick and return card
	card = chance_cards.pop(0)
	chance_cards.append(card)

	# exact position cards
	if isinstance(card, int): return card

	# next r_card
	if card == "next_r":
		# railroad @ 5, 15, 25, 35
		# card positions: position == 7 or position == 22 or position == 36:
		if position == 7  : return 15
		if position == 22 : return 25
		if position == 36 : return 5

	# next_u card
	if card == "next_u":
		# utilities @ 12 and 28
		if 13 <= position <= 27: return 28
		return 12

	# back_3
	if card == "back_3":
		position -= 3
		return position

	# default: nop cards
	return position
	
def community_chest(position):
	""" Returns new position based on community chest card in stack """
	# pick and return card
	card = community_chest_cards.pop(0)
	community_chest_cards.append(card)

	# a new position card?
	if isinstance(card, int): return card

	# if not a new position: nop card
	return position

def roll_dice():
	""" Returns both number and 'doubles' of two dice rolls """
	# (1,6) is normal dice
	# (1,4) is pe requested dice
	dice1 = randint(1,6)
	dice2 = randint(1,6)
	# return both number and doubles...
	return dice1 + dice2, dice1 == dice2

# simulate 
for n in range(1000000):

	doubles_streak = 0
	first_run = True # first run is to emulate do while loop
	while doubles_streak or first_run:

		#assert(doubles_streak <= 3)

		# no longer first run
		first_run = False

		# roll dice
		number, doubles  = roll_dice()

		# either our doubles streak continues or exit next time
		if doubles : doubles_streak += 1
		else: doubles_streak = 0

		# calc new position
		position = (position + number) % 40

		# trice doubles g2j rule
		# NB: end double_streak in 'position == 10' end of loop
		if doubles_streak == 3:  position = 10 

		# rule g2j
		if position == 30 : position = 10

		# rule chance, before community chest, as 36 and back-3 can give 33
		if position == 7 or position == 22 or position == 36:
			position = chance(position)

		# rule community chest
		if position == 2 or position == 17 or position == 33:
			position = community_chest(position)

		# update square hit counter
		square_hit_counter[position] += 1

		# if we hit jail also reset double continue
		if position == 10 : doubles_streak = 0


# filter results
first = max(square_hit_counter, key=square_hit_counter.get)
square_hit_counter[first] = 0 # remove to find new max
second = max(square_hit_counter, key=square_hit_counter.get)
square_hit_counter[second] = 0
third = max(square_hit_counter, key=square_hit_counter.get)

print(first)
print(second)
print(third)