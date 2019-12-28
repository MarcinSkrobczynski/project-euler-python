# Utilities to Project Euler Problems
# Copyright (c) MarcinSkrobczynski


def is_palindrome(x: int) -> bool:
    digits = str(x)
    return digits == digits[::-1]
