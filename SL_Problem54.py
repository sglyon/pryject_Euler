"""
Created Mar 11, 2013

Author: Spencer Lyon

Project Euler Problem 54:

In the card game poker, a hand consists of five cards and are ranked,
from lowest to highest, in the following way:

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

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the
highest value wins; for example, a pair of eights beats a pair of fives
(see example 1 below). But if two ranks tie, for example, both players
have a pair of queens, then highest cards in each hand are compared
(see example 4 below); if the highest cards tie then the next highest
cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two
players. Each line of the file contains ten cards (separated by a single
space): the first five are Player 1's cards and the last five are
Player 2's cards. You can assume that all hands are valid (no invalid
characters or repeated cards), each player's hand is in no specific
order, and in each hand there is a clear winner.

How many hands does Player 1 win?
"""
from __future__ import division
from time import time
import re
import pandas as pd
import numpy as np


def rank_hand(x):
    flush = True
    suit_1 = x[0][1]
    for i in x:
        if i[1] != suit_1:
            flush = False

    nums = [int(i[0]) for i in x]
    nums.sort()
    nums = pd.Series(nums)
    counts = nums.value_counts()
    counts.sort()

    straight = True if (nums.diff(1)[1:] == 1).sum() == 4 else False

    if straight == True:
        if flush == False:
            return 'straight'
        else:
            return 'royal_flush' if nums.min() == 10 else 'straight_flush'

    # else for not straight isn't necessary because the if always returns
    if flush == True:
        return 'flush'

    if counts.max() == 3:
        if counts.min() == 2:
            return 'full_house'
        else:
            return 'three_kind'

    elif counts.max() == 2:
        if counts.value_counts().max() == 2:
            return 'two_pair'
        else:
            return 'pair'

    elif counts.max() == 4:
        return 'four_kind'

    else:  # All unique cards. Not straight, not flush, our multiple card hand
        return 'high_card'


def compare_single(x, y):
    """
    This function is to be called when you need to find the single
    high card amongst two hands.

    Parameters
    ----------
    x, y: pd.Series, dtype=int
        pandas Series objects that contain the integers for the
        hand

    Returns
    -------
    res: int
        The result, or the winner. It is equal to 1 if the player
        corresponding to hand x wins, and 0 if hand y wins'
    """
    if x.max() > y.max():
        return 1
    elif x.max() < y.max():
        return 0
    else:
        sortx = np.sort(x)[::-1]
        sorty = np.sort(y)[::-1]
        compare_single(sortx[1:], sorty[1:])


def compare_double(x, y):
    """
    This function is to be called when you need to find the winning
    hand when both players have a pair (or two pairs).

    Parameters
    ----------
    x, y: pd.Series, dtype=int
        pandas Series objects that contain the integers for the
        hand

    Returns
    -------
    res: int
        The result, or the winner. It is equal to 1 if the player
        corresponding to hand x wins, and 0 if hand y wins'
    """
    countx = x.value_counts()
    county = y.value_counts()

    if countx[countx == 2].index[0] > county[county == 2].index[0]:
        return 1
    elif countx[countx == 2].index[0] < county[county == 2].index[0]:
        return 0
    else:  # tie for high pair
        if countx[countx == 2].size == 2:  # See if we have two pairs
            if countx[countx == 2].index[1] > county[county == 2].index[1]:
                return 1
            elif countx[countx == 2].index[1] < county[county == 2].index[1]:
                return 0
            else:  # b/c we had two pairs, only 1 item with value_count = 1
                if countx[countx == 1].index[0] > county[county == 1].index[0]:
                    return 1
                else:
                    return 0
        else:  # now compare 3 single cards
            return compare_single(countx[countx == 1].index,
                                  county[county == 1].index)


def compare_triple_or4(x, y):
    """
    This function is to be called when you need to find the winning
    hand when both players have three or four of a kind.

    Parameters
    ----------
    x, y: pd.Series, dtype=int
        pandas Series objects that contain the integers for the
        hand

    Returns
    -------
    res: int
        The result, or the winner. It is equal to 1 if the player
        corresponding to hand x wins, and 0 if hand y wins'
    """
    countx = x.value_counts()
    county = y.value_counts()

    if countx.index[0] > county.index[0]:
        return 1
    elif countx.index[0] < county.index[0]:
        return 0

    # NOTE: This takes care of it because they can't both of 3/4 of a same #
    #       because there are only 4 of each card in a deck.


def compare_full(x, y):
    """
    This function is to be called when you need to find the winning
    hand when both players have a full house.

    Parameters
    ----------
    x, y: pd.Series, dtype=int
        pandas Series objects that contain the integers for the
        hand

    Returns
    -------
    res: int
        The result, or the winner. It is equal to 1 if the player
        corresponding to hand x wins, and 0 if hand y wins'
    """
    count1 = x.value_counts()
    count2 = y.value_counts()

    if count1.index[0] > count2.index[0]:
        return 1
    elif count1.index[0] < count2.index[0]:
        return 0
    else:
        if count1.index[1] > count2.index[1]:
            return 1
        elif count1.index[1] < count2.index[1]:
            return 0


def compare_stright(x, y):
    """
    This function is to be called when you need to find the winning
    hand when both players have a straight (or straight flush).

    Parameters
    ----------
    x, y: pd.Series, dtype=int
        pandas Series objects that contain the integers for the
        hand

    Returns
    -------
    res: int
        The result, or the winner. It is equal to 1 if the player
        corresponding to hand x wins, and 0 if hand y wins'
    """
    # Must have a different starting number per problem desc (no ties)
    return 1 if x.max() > y.max() else 0


def pick_winner(x):
    p1 = x[:5]
    p2 = x[5:-1]  # Go to -1 to not take 'winner' column

    hand1 = rank_hand(p1)
    hand2 = rank_hand(p2)

    rank1 = ranks[hand1]
    rank2 = ranks[hand2]

    if rank1 > rank2:
        x['winner'] = 1
    elif rank1 < rank2:
        x['winner'] = 0
    else:  # Same rank
        nums1 = p1.str.get(0).astype(int)
        nums2 = p2.str.get(0).astype(int)

        if hand1 == 'high_card':
            x['winner'] = compare_single(nums1, nums2)

        elif hand1 == 'pair':
            x['winner'] = compare_double(nums1, nums2)

        elif hand1 == 'two_pair':
            x['winner'] = compare_double(nums1, nums2)

        elif hand1 == 'three_kind':
            x['winner'] = compare_triple_or4(nums1, nums2)

        elif hand1 == 'straight':
            x['winner'] = compare_stright(nums1, nums2)

        elif hand1 == 'flush':  # Get highest card
            x['winner'] = compare_single(nums1, nums2)

        elif hand1 == 'full_house':
            x['winner'] = compare_full(nums1, nums2)

        elif hand1 == 'four_kind':
            x['winner'] = compare_triple_or4(nums1, nums2)

        elif hand1 == 'straight_flush':
            x['winner'] = compare_single(nums1, nums2)

        elif hand1 == 'royal_flush':
            print('Look up which suit dominates')

    return x

start_time = time()

hands = pd.read_table('poker.txt', sep=' ', header=None)

cols = ['p11', 'p12', 'p13', 'p14', 'p15',
        'p21', 'p22', 'p23', 'p24', 'p25']

suits = {'S': 'spades', 'D': 'diamonds', 'H': 'hearts', 'C': 'clubs'}
faces = {'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
ranks = {'high_card': 1, 'pair': 2, 'two_pair': 3, 'three_kind': 4,
         'straight': 5, 'flush': 6, 'full_house': 7, 'four_kind': 8,
         'straight_flush': 9, 'royal_flush': 10}

hands = hands.rename_axis(dict(enumerate(cols)))
rex = re.compile(r'(\d+)(\w)')

for i in cols:
    hands[i] = hands[i].str[0].replace(faces.keys(),
                           faces.values()).astype(str) + hands[i].str[1]
    hands[i] = hands[i].str.match(rex)

hands['winner'] = np.nan

hands = hands.apply(pick_winner, axis=1)

ans = int(hands.winner.sum())

print("The answer is: %i" % (ans))

running_time = time()
elapsed_time = running_time - start_time
print 'Total Execution time is ', elapsed_time, 'seconds'

if __name__ == '__main__':
    single = [(8, 'C'), (4, 'D'), (10, 'C'), (11, 'C'), (12, 'C')]
    two = [(8, 'C'), (8, 'D'), (10, 'C'), (11, 'C'), (12, 'C')]
    three = [(8, 'C'), (8, 'D'), (8, 'H'), (11, 'C'), (12, 'C')]
    four = [(8, 'C'), (8, 'D'), (8, 'H'), (8, 'S'), (12, 'C')]
    two_pair = [(8, 'C'), (8, 'D'), (10, 'C'), (11, 'C'), (10, 'H')]
    full = [(8, 'C'), (8, 'S'), (8, 'D'), (11, 'C'), (11, 'H')]
    straight_flush = [(8, 'C'), (9, 'C'), (10, 'C'), (11, 'C'), (12, 'C')]
    straight = [(13, 'C'), (14, 'C'), (10, 'C'), (11, 'C'), (12, 'D')]
    royal_flush = [(13, 'C'), (14, 'C'), (10, 'C'), (11, 'C'), (12, 'C')]
    flush = hand3 = [(5, 'C'), (14, 'C'), (10, 'C'), (11, 'C'), (12, 'C')]

