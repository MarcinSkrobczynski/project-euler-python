# Solution to Project Euler Problem #26: Reciprocal cycles
# Copyright (c) MarcinSkrobczynski

from itertools import count


def reciprocal_cycle(n: int) -> int:
    remains = {}
    x = 1
    for i in count():
        if x == 0:
            return 0
        elif x in remains:
            return i - remains[x]
        else:
            remains[x] = i
            x = (x * 10) % n


def main(start: int, stop: int) -> int:
    return max(range(start, stop + 1), key=reciprocal_cycle)


def solution() -> int:
    return main(2, 999)


if __name__ == "__main__":
    print(f"{main(2, 10)} => {main(2, 10) == 6}")
    print(f"{main(2, 999)}")
