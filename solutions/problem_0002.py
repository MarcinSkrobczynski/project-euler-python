# Solution to Project Euler Problem #2: Even Fibonacci numbers
# Copyright (c) MarcinSkrobczynski


def main(n: int):
    sums = 0
    old = curr = 1
    while curr < n:
        if curr % 2 == 0:
            sums += curr

        old, curr = curr, old + curr

    return sums


def solution():
    return main(4000000)


if __name__ == "__main__":
    print(f"{main(100)} => {main(100) == 44}")  # 44 = 2 + 8 + 34
    print(f"{main(4000000)}")
