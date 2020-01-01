# Solution to Project Euler Problem #4: Largest palindrome product
# Copyright (c) MarcinSkrobczynski

from solutions.utils import is_palindrome


def main(n: int):
    return max(i * j for i in range(n, 0, -1) for j in range(n, 0, -1) if is_palindrome(i * j))


def solution():
    return main(999)


if __name__ == "__main__":
    print(f"{main(99)} => {main(99) == 9009}")
    print(f"{main(999)}")
