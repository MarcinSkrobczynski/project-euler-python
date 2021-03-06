# Solution to Project Euler Problem #15: Lattice paths
# Copyright (c) MarcinSkrobczynski


def main(x: int, y: int) -> int:
    result = 1

    mini = min(x, y)
    maxi = max(x, y)

    for i in range(maxi + 1, mini + maxi + 1):
        result *= i
        result //= (i - maxi)

    return result


def solution() -> int:
    return main(20, 20)


if __name__ == "__main__":
    print(f"{main(2, 2)} => {main(2, 2) == 6}")
    print(f"{main(20, 20)}")
