#!/usr/bin/python3
"""This program solves the N queens problem."""
import sys


def is_safe(queens, row, col):
    """Checks if a position is safe for placement"""
    for q_row, q_col in queens:
        if (q_col == col or q_row + q_col == row + col or
                q_row - q_col == row - col):
            return False
    return True


def solve(queens, row, n):
    """Main recursive function"""
    if row == n:
        print(queens)
        return
    for col in range(n):
        if is_safe(queens, row, col):
            solve(queens + [[row, col]], row + 1, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)

    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    solve([], 0, int(sys.argv[1]))
