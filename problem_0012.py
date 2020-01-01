# Solution to Project Euler Problem #12: Highly divisible triangular number
# Copyright (c) MarcinSkrobczynski

from itertools import count
from math import sqrt


def get_num_of_factors(n: int) -> int:
    upper = int(sqrt(n))
    number = sum(2 for i in range(1, upper + 1) if n % i == 0)
    if upper ** 2 == n:
        number -= 1
    return number


def main(n: int):
    triangle_number = 0
    for i in count(1):
        triangle_number += i
        if get_num_of_factors(triangle_number) > n:
            return triangle_number
    return 0


if __name__ == "__main__":
    print(f"{main(5)} => {main(5) == 28}")
    print(f"{main(500)}")
