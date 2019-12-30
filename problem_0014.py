# Solution to Project Euler Problem #14: Longest Collatz sequence
# Copyright (c) MarcinSkrobczynski

import functools


@functools.lru_cache(maxsize=None)
def collatz_sequence(n: int) -> int:
    if n == 1:
        return 1

    if n % 2 == 0:
        m = n // 2
    else:
        m = 3 * n + 1

    return collatz_sequence(m) + 1


def main():
    return max(range(1, 1000000), key=collatz_sequence)


if __name__ == "__main__":
    print(f"{main()}")