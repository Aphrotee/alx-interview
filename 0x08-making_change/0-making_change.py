#!/usr/bin/python3

"""
This module provides the `makeChange` function
"""


def makeChange(coins, total):
    """
    This function returns fewest number of coins needed to meet total
    """
    if coins is None or total is None:
        return -1
    if len(coins) <= 0:
        return 0
    count, totalCount = 0, 0
    i = len(coins) - 1
    coins.sort()
    while total > 0:
        if i < 0:
            return -1
        if coins[i] < total:
            count = total // coins[i]
            totalCount += count
            total -= (count * coins[i])
        i -= 1
    return totalCount
