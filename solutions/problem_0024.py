# Solution to Project Euler Problem #24: Lexicographic permutations
# Copyright (c) MarcinSkrobczynski

import itertools


def main(n: int, i: int) -> int:
    permutation = itertools.islice(itertools.permutations(range(n)), i - 1, None)
    return int("".join(str(d) for d in next(permutation)))


def solution() -> int:
    return main(10, 1000000)


if __name__ == "__main__":
    print(f"{main(3, 4)} => {main(3, 4) == 120}")
    print(f"{main(3, 6)} => {main(3, 6) == 210}")
    print(f"{main(10, 1000000)}")
