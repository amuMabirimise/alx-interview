#!/usr/bin/python3
"""A functioning determining the fewest number of coins needed
   to meet a given amount total"""


def makeChange(coins, total):
    """This function's will take a list of a coins and use
       that is to calculate how much change the total will require
    """
    if total <= 0:
        return 0

    else:
        coin = sorted(coins)
        coin.reverse()
        counter = 0
        for i in coin:
            while(total >= i):
                counter += 1
                total -= i
        if total == 0:
            return counter
        return -1