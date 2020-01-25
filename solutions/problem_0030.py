# Solution to Project Euler Problem #30: Digit fifth powers
# Copyright (c) MarcinSkrobczynski


def is_sum_of_nth_power_of_digits(n: int, power: int) -> bool:
    return n == sum(int(digit)**power for digit in str(n))


def main(n: int, power: int) -> int:
    return sum(i for i in range(2, n) if is_sum_of_nth_power_of_digits(i, power))


def solution() -> int:
    return main(1000000, 5)


if __name__ == "__main__":
    print(f"{main(10000, 4)} => {main(10000, 4) == 19316}")
    print(f"{main(1000000, 5)}")
