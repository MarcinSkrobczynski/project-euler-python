# Solution to Project Euler Problem #14: Longest Collatz sequence
# Copyright (c) MarcinSkrobczynski

import functools

BELOW_TWENTY = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
                "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]

DOZENS_ABOVE_TEN = ["twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

HUNDRED = "hundred"

AND = "and"


@functools.lru_cache(maxsize=None)
def get_number_words_length(n: int) -> int:
    if n > 1000:
        raise NotImplementedError

    if n == 0:
        return 0

    if n == 1000:
        return len("one") + len("thousand")

    if n < 20:
        return len(BELOW_TWENTY[n - 1])

    if n < 100:
        return len(DOZENS_ABOVE_TEN[n // 10 - 2]) + (len(BELOW_TWENTY[n % 10 - 1]) if n % 10 > 0 else 0)

    result = get_number_words_length(n // 100) + len(HUNDRED) + get_number_words_length(n % 100)

    if n // 100 > 0 and n % 100 > 0:
        result += len(AND)

    return result


def main(n: int):
    return sum(get_number_words_length(x) for x in range(1, n + 1))


if __name__ == "__main__":
    print(f"{get_number_words_length(342)} => {get_number_words_length(342) == 23}")
    print(f"{get_number_words_length(115)} => {get_number_words_length(115) == 20}")
    print(f"{main(5)} => {main(5) == 19}")
    print(f"{main(1000)}")
