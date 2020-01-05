# Solution to Project Euler Problem #23: Non-abundant sums
# Copyright (c) MarcinSkrobczynski

from solutions.utils import get_sums_of_divisors


def main(n: int) -> int:
    sums_of_divisors = get_sums_of_divisors(n)
    abundant = [i for (i, j) in enumerate(sums_of_divisors) if j > i]
    sums = {i + j for i in abundant for j in abundant if i + j <= n}
    valid_numbers = [i for i in range(1, n + 1) if i not in sums]
    return sum(valid_numbers)


def solution() -> int:
    return main(28123)


if __name__ == "__main__":
    print(f"{main(28123)}")
