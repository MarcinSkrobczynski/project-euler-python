# Solution to Project Euler Problem #6: Sum square difference
# Copyright (c) MarcinSkrobczynski


def main(n: int):
    numbers = [x for x in range(1, n+1)]
    sum_of_squares = sum([x*x for x in numbers])
    square_of_sums = sum(numbers) ** 2
    return square_of_sums - sum_of_squares


if __name__ == "__main__":
    print(f"{main(10)} => {main(10) == 2640}")
    print(f"{main(100)}")
