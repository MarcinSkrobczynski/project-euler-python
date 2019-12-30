# Solution to Project Euler Problem #16: Power digit sum
# Copyright (c) MarcinSkrobczynski


def main(n: int):
    return sum(int(x) for x in str(n))


if __name__ == "__main__":
    print(f"{main(2 ** 15)} => {main(2 ** 15) == 26}")
    print(f"{main(2 ** 1000)}")
