# Solution to Project Euler Problem #10: Summation of primes
# Copyright (c) MarcinSkrobczynski


from solutions.utils import get_primes


def main(n: int) -> int:
    return sum(list(get_primes(n)))


def solution() -> int:
    return main(2000000)


if __name__ == "__main__":
    print(f"{main(10)} => {main(10) == 17}")
    print(f"{main(2000000)}")
