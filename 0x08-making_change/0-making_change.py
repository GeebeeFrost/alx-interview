#!/usr/bin/python3
"""This script contains the makeChange function."""


def makeChange(coins, total):
    """
    This function makes change for a given total using the fewest coins.

    Args:
        coins: list of the values of the coins available.
        total: the total to make change for.

    Returns:
        The fewest number of coins needed to meet total.
        If the total cannot be made with the coins available, return -1.
    """
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    num_coins = 0
    for coin in coins:
        if total <= 0:
            break
        num_coins += total // coin
        total = total % coin
    if total != 0:
        return -1
    return num_coins
