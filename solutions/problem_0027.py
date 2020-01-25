# Solution to Project Euler Problem #27: Quadratic primes
# Copyright (c) MarcinSkrobczynski

from itertools import count

from solutions.utils import is_prime


def number_of_consecutive_quadratic_primes(ab: tuple):
    a, b = ab
    for n in count():
        number = n ** 2 + a * n + b
        if not is_prime(number):
            return n


def main(min_a: int, max_a: int, min_b: int, max_b: int) -> int:
    pair = max(((a, b) for a in range(min_a, max_a + 1) for b in range(min_b, max_b + 1)),
               key=number_of_consecutive_quadratic_primes)
    return pair[0] * pair[1]


def solution() -> int:
    return main(-999, 999, -1000, 1000)


if __name__ == "__main__":
    print(f"{number_of_consecutive_quadratic_primes((1, 41))} => "
          f"{number_of_consecutive_quadratic_primes((1, 41)) == 40}")
    print(f"{number_of_consecutive_quadratic_primes((-79, 1601))} => "
          f"{number_of_consecutive_quadratic_primes((-79, 1601)) == 80}")
    print(f"{main(-999, 999, -1000, 1000)}")
