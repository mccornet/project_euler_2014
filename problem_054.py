from itertools import groupby
from operator  import itemgetter

"""
    High Card: Highest value card.
    One Pair: Two cards of the same value.
    Two Pairs: Two different pairs.
    Three of a Kind: Three cards of the same value.
    Straight: All cards are consecutive values.
    Flush: All cards of the same suit.
    Full House: Three of a kind and a pair.
    Four of a Kind: Four cards of the same value.
    Straight Flush: All cards are consecutive values of same suit.
    Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
"""

ratings = dict()

ratings['royal_flush']   = 10*10**10
ratings['straigt_flush'] = 9*10**10
ratings['4_of_a_kind']   = 8*10**10
ratings['full_house']    = 7*10**10
ratings['flush']         = 6*10**10
ratings['straight']      = 5*10**10
ratings['3_of_a_kind']   = 4*10**10
ratings['two_pairs']     = 3*10**10
ratings['pair']          = 2*10**10
ratings['high_card']     = 1*10**10

def rate_poker_hand(hand):

    # dicts for processings
    suits = dict()
    ranks = dict()

    ranks_ordered = []
    straigt_detected = False
    straigt_highest = 0

    # filter suits and ranks into dicts and lists
    for card in hand:
        # fill suit dict
        suit = card[-1]
        if suit not in suits : suits[suit] = 0 # init dict
        suits[suit] = suits[suit] + 1

        # print(suits[suit])

        # fill rank dict and list
        rank = card[0:-1] # get rank

        rank = rank.replace('A','14').replace('K','13')\
                   .replace('Q','12').replace('J','11').replace('T','10')

        if rank not in ranks : ranks[rank] = 0 # init dict
        ranks[rank] = ranks[rank] + 1

        ranks_ordered.append(int(rank))

    # perform order operation
    ranks_ordered.sort()

    # detect straigt, ace value is 14
    if ranks_ordered[4] - ranks_ordered[3] == ranks_ordered[3] - ranks_ordered[2] == \
        ranks_ordered[2] - ranks_ordered[1] == ranks_ordered[1] - ranks_ordered[0] == 1 :

        straigt_detected, straigt_highest = True, ranks_ordered[4]

    # detect straigt, ace value is 1
    ranks_ordered_2 = [1 if rank == 14 else rank for rank in ranks_ordered]
    ranks_ordered_2.sort()

    if ranks_ordered_2[4] - ranks_ordered_2[3] == ranks_ordered_2[3] - ranks_ordered_2[2] == \
        ranks_ordered_2[2] - ranks_ordered_2[1] == ranks_ordered_2[1] - ranks_ordered_2[0] == 1 :

        straigt_detected, straigt_highest = True, ranks_ordered_2[4]
    # preperations are done, time to return the ranking of the hand!

    # RETURN flush
    if len(suits) == 1: # only one suit

        #print("flush detected")

        # ROYAL FLUSH
        if straigt_detected and straigt_highest == 14: return ratings['royal_flush']

        # Straight flush
        if straigt_detected: return ratings['straigt_flush'] + straigt_highest*10**2

        # regular flush
        return ratings['flush'] + ranks_ordered[4]*10**2

    # RETURN 4 of a kind
    if any(rank_count == 4 for rank_count in ranks.values()):

        #print("4 o a k")

        # find rank
        rank_4, rank_1 = 0, 0

        for rank, rank_count in ranks.items():
            if rank_count == 1 : rank_1 = rank
            if rank_count == 4 : rank_4 = rank

        return ratings['4_of_a_kind'] + rank_4 *10**2 + rank_1

    # RETURN full house
    if (any(rank == 3 for rank in ranks.values()) and \
        any(rank == 2 for rank in ranks.values()) ):

        #print("full house")

        # find rank
        rank_3, rank_2 = 0, 0

        for rank, rank_count in ranks.items():
            if rank_count == 2 : rank_2 = rank
            if rank_count == 3 : rank_3 = rank

        return ratings['full_house'] + int(rank_3)*10**2 + int(rank_2)

    # RETURN straight (not flush)
    if straigt_detected :
        #print("straigt")
        return ratings['straight'] + straigt_highest

    # RETURN 3 of a kind
    if any(rank == 3 for rank in ranks.values()) :

        #print("3 of a kind")

        rank_3 = 0
        for rank, rank_count in ranks.items():
            if rank_count == 3 : rank_3 = rank

        other_cards = list(set(ranks_ordered))
        other_cards.remove(int(rank_3))

        return ratings['3_of_a_kind'] + max(other_cards)*10**2 + min(other_cards)

    # RETURN 2 pair
    if len(ranks) == 3 :

        #print("2 pair")

        pair_cards = []

        for rank, count in ranks.items():
            if count == 2 : pair_cards.append(int(rank))

        single_card = list(set(ranks_ordered) - set(pair_cards))

        return ratings['two_pairs'] + max(pair_cards)*10**4 + min(pair_cards)*10**2 + single_card[0]

    # RETURN 1 pair
    if len(ranks) == 4 :

        #print("one pair")

        # find pair card
        pair_card = 0
        for rank, count in ranks.items():
            if count == 2 : pair_card = rank

        single_cards = list(set(ranks_ordered) - set([int(pair_card)]))
        single_cards.sort()

        return ratings['pair']  + int(pair_card)*10**6 + single_cards[2]*10**4 \
                                + single_cards[1]*10**2 + single_cards[0]

    # RETURN high card
    if len(ranks) == 5 :

        #print("high card")

        return ratings['high_card'] + ranks_ordered[4]*10**8 + ranks_ordered[3]*10**6 + \
                                      ranks_ordered[2]*10**4 + ranks_ordered[1]*10**2 + \
                                      ranks_ordered[0]
    # RETURN error
    return 0


# read file into lines
poker_hands = [line.rstrip('\n') for line in open("problem_54.txt")]



count_player_1_win = 0
n = 1

for pair_of_hands in poker_hands:

    # filter into two lists, each with individual cards!
    cards = pair_of_hands.split(" ")
    hand_1 = cards[:5]
    hand_2 = cards[-5:]

    print(n, ": ", hand_1, hand_2)
    n += 1

    rate_1, rate_2 = rate_poker_hand(hand_1), rate_poker_hand(hand_2)
    #print(rate_1, rate_2)

    if rate_1 > rate_2 :
        count_player_1_win += 1
        print("player 1 win")
    else:
        print("player 2 win")


print("times player 1 wins:",count_player_1_win)

