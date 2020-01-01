# Solution to Project Euler Problem #7: 10001st prime
# Copyright (c) MarcinSkrobczynski

from solutions.utils import get_primes, get_upper_bound_for_nth_prime


def main(n: int):
    upper = get_upper_bound_for_nth_prime(n)
    primes = list(get_primes(upper))
    return primes[n - 1]


def solution():
    return main(10001)


if __name__ == "__main__":
    print(f"{main(6)} => {main(6) == 13}")
    print(f"{main(10001)}")
