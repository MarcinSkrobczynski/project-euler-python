# Utilities to Project Euler Problems
# Copyright (c) MarcinSkrobczynski

from math import gcd


def is_palindrome(x: int) -> bool:
    digits = str(x)
    return digits == digits[::-1]


def lcm(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)


def lcm_iter(x: list) -> int:
    numbers = x.copy()
    number = numbers.pop()

    for i in numbers:
        number = lcm(number, i)

    return number
