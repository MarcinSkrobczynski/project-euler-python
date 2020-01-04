# Solution to Project Euler Problem #3: Largest prime factor
# Copyright (c) MarcinSkrobczynski

from math import sqrt


def main(n: int) -> int:
    max_prime = int(sqrt(n))
    num = n
    i = 0

    while num % 2 == 0:
        num //= 2

    for i in range(3, max_prime, 2):
        while num % i == 0:
            num //= i
        if num == 1:
            break

    return i


def solution() -> int:
    return main(600851475143)


if __name__ == "__main__":
    print(f"{main(13195)} => {main(13195) == 29}")
    print(f"{main(600851475143)}")
