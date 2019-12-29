# Solution to Project Euler Problem #10: Summation of primes
# Copyright (c) MarcinSkrobczynski


def get_primes(upper_bound: int):
    numbers = [True] * upper_bound
    numbers[0] = numbers[1] = False

    for (i, is_prime) in enumerate(numbers):
        if is_prime:
            yield i
            for n in range(i * i, upper_bound, i):
                numbers[n] = False


def main(n: int):
    return sum(list(get_primes(n)))


if __name__ == "__main__":
    print(f"{main(10)} => {main(10) == 17}")
    print(f"{main(2000000)}")
