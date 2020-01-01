# Solution to Project Euler Problem #21: Amicable numbers
# Copyright (c) MarcinSkrobczynski

from solutions.utils import get_sum_of_divisors


def main(n: int):
    if n < 10:
        return 0
    numbers = {x: (get_sum_of_divisors(x, False), False) for x in range(0, n)}
    result = 0
    for i, (p, is_amicable) in numbers.items():
        if i == p or is_amicable or p >= n:
            continue
        if numbers[p][0] == i:
            result += i + p
            numbers[p] = (i, True)
            numbers[i] = (p, True)
    return result


def solution():
    return main(10000)


if __name__ == "__main__":
    print(f"{get_sum_of_divisors(1)} => {get_sum_of_divisors(1) == 1}")
    print(f"{get_sum_of_divisors(1, False)} => {get_sum_of_divisors(1, False) == 0}")
    print(f"{get_sum_of_divisors(4)} => {get_sum_of_divisors(4) == 7}")
    print(f"{get_sum_of_divisors(4, False)} => {get_sum_of_divisors(4, False) == 3}")
    print(f"{get_sum_of_divisors(220, False)} => {get_sum_of_divisors(220, False) == 284}")
    print(f"{get_sum_of_divisors(284, False)} => {get_sum_of_divisors(284, False) == 220}")
    print(f"{main(10000)}")
