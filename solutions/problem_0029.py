# Solution to Project Euler Problem #29: Distinct powers
# Copyright (c) MarcinSkrobczynski


def get_distinct_terms(a_min: int, a_max: int, b_min: int, b_max: int) -> set:
    return {a ** b for a in range(a_min, a_max + 1) for b in range(b_min, b_max + 1)}


def main(a_min: int, a_max: int, b_min: int, b_max: int) -> int:
    return len(get_distinct_terms(a_min, a_max, b_min, b_max))


def solution() -> int:
    return main(2, 100, 2, 100)


if __name__ == "__main__":
    print(f"{main(2, 5, 2, 5)} => {main(2, 5, 2, 5) == 15}")
    print(f"{main(2, 100, 2, 100)}")
