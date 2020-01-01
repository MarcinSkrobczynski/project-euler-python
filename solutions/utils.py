# Utilities to Project Euler Problems
# Copyright (c) MarcinSkrobczynski

from math import gcd, ceil, log, sqrt


def is_palindrome(x: int) -> bool:
    digits = str(x)
    return digits == digits[::-1]


def lcm(x: int, y: int) -> int:
    return (x * y) // gcd(x, y)


def get_num_of_divisors(n: int, i: bool = None) -> int:
    upper = int(sqrt(n))
    include = True if i is None else bool(i)
    number = sum(2 for i in range(1, upper + 1) if n % i == 0)
    if upper ** 2 == n:
        number -= 1 if include else 2
    return number


def get_sum_of_divisors(n: int, ie: bool = None) -> int:
    upper = int(sqrt(n))
    include = True if ie is None else bool(ie)
    if n == 0:
        return 0
    if n == 1:
        return 1 if include else 0
    number = 1
    number += sum((i + n // i) if i * i != n else i for i in range(2, upper + 1) if n % i == 0)
    if include:
        number += n
    return number


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
