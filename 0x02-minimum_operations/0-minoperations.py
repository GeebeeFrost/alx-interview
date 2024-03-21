#!/usr/bin/python3
"""This script contains the minOperations method."""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to result in exactly
    n H characters in a file.
    """
    ops = 0
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            ops += i
    if n > 1:
        ops += n
    return ops
