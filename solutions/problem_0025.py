# Solution to Project Euler Problem #25: 1000-digit Fibonacci number
# Copyright (c) MarcinSkrobczynski

from itertools import count


def main(n: int) -> int:
    prev = 1
    curr = 0
    for i in count():
        if len(str(curr)) >= n:
            return i

        prev, curr = curr, prev + curr
    return 0


def solution() -> int:
    return main(1000)


if __name__ == "__main__":
    print(f"{main(3)} => {main(3) == 12}")
    print(f"{main(1000)}")
