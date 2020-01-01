# Utilities to Project Euler Problems
# Copyright (c) MarcinSkrobczynski

from math import gcd, ceil, log


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


def get_upper_bound_for_nth_prime(n: int) -> int:
    """
    https://en.wikipedia.org/wiki/Prime_number_theorem
    """
    if n < 6:
        return 15
    return ceil(n * (log(n) + log(log(n))))


def get_primes(upper_bound: int):
    numbers = [True] * (upper_bound + 1)
    numbers[0] = numbers[1] = False

    for (i, is_prime) in enumerate(numbers):
        if is_prime:
            yield i
            for n in range(i * i, upper_bound + 1, i):
                numbers[n] = False
