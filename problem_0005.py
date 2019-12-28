# Solution to Project Euler Problem #5: Smallest multiple
# Copyright (c) MarcinSkrobczynski

from utils import lcm_iter


def main(n: int):
    return lcm_iter([x for x in range(1, n + 1)])


if __name__ == "__main__":
    print(f"{main(10)} => {main(10) == 2520}")
    print(f"{main(20)}")
