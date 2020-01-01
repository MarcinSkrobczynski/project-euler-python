# Solution to Project Euler Problem #20: Factorial digit sum
# Copyright (c) MarcinSkrobczynski

from math import factorial


def main(n: int):
    return sum(int(x) for x in str(n))


def solution():
    return main(factorial(100))


if __name__ == "__main__":
    print(f"{main(factorial(10))} => {main(factorial(10)) == 27}")
    print(f"{main(factorial(100))}")
