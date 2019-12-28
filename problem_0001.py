# Solution to Project Euler Problem #1: Multiples of 3 and 5
# Copyright (c) MarcinSkrobczynski


def main(n: int):
    return sum(x for x in range(n) if (x % 3 == 0 or x % 5 == 0))


if __name__ == "__main__":
    print(f"{main(10)} => {main(10) == 23}")
    print(f"{main(1000)}")
