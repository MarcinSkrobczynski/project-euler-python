# Solution to Project Euler Problem #9: Special Pythagorean triplet
# Copyright (c) MarcinSkrobczynski


def main(n: int):
    for a in range(1, n + 1):
        for b in range(a + 1, n + 1 - a):
            c = n - a - b
            if b >= c or c * c != a * a + b * b:
                continue
            return a * b * c
    return 0


if __name__ == "__main__":
    print(f"{main(12)} => {main(12) == 60}")
    print(f"{main(1000)}")
