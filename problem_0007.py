# Solution to Project Euler Problem #7: 10001st prime
# Copyright (c) MarcinSkrobczynski

from math import log, ceil


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


def main(n: int):
    upper = get_upper_bound_for_nth_prime(n)
    primes = list(get_primes(upper))
    return primes[n - 1]


if __name__ == "__main__":
    print(f"{main(6)} => {main(6) == 13}")
    print(f"{main(10001)}")
