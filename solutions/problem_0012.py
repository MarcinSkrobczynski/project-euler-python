# Solution to Project Euler Problem #12: Highly divisible triangular number
# Copyright (c) MarcinSkrobczynski

from itertools import count

from solutions.utils import get_num_of_divisors


def main(n: int) -> int:
    triangle_number = 0
    for i in count(1):
        triangle_number += i
        if get_num_of_divisors(triangle_number) > n:
            return triangle_number
    return 0


def solution() -> int:
    return main(500)


if __name__ == "__main__":
    print(f"{main(5)} => {main(5) == 28}")
    print(f"{main(500)}")
