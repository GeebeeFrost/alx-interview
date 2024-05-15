#!/usr/bin/python3
"""
This script contains the primeNumbers and isWinner functions.
"""


def primeNumbers(n):
    """Return list of prime numbers between 1 and n inclusive
       Args:
        n (int): upper boundary of range. lower boundary is always 1
    """
    result = []
    initial = [True] * (n + 1)
    for i in range(2, n + 1):
        if (initial[i]):
            result.append(i)
            for j in range(i, n + 1, i):
                initial[j] = False
    return result


def isWinner(x, nums):
    """
    Returns the winner of the prime game
    Args:
        x (int): the number of rounds
        nums (list): a list of n integers
    Returns:
        str: the name of the player that won the most rounds
    """
    if not x or len(nums) < 1:
        return None
    Maria = Ben = 0
    for i in range(x):
        primes = primeNumbers(nums[i])
        if len(primes) % 2 == 0:
            Ben += 1
        else:
            Maria += 1
    if Maria > Ben:
        return 'Maria'
    elif Ben > Maria:
        return 'Ben'
    return None
