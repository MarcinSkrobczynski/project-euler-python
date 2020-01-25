# Solution to Project Euler Problem #28: Number spiral diagonals
# Copyright (c) MarcinSkrobczynski


def main(n: int) -> int:
    return 1 + sum(16 * i * i + 4 * i + 4 for i in range(1, n // 2 + 1))


def solution() -> int:
    return main(1001)


if __name__ == "__main__":
    print(f"{main(5)} => {main(5) == 101}")
    print(f"{main(1001)}")
