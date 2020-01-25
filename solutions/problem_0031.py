# Solution to Project Euler Problem #31: Coin sums
# Copyright (c) MarcinSkrobczynski

ALL_COINS = [1, 2, 5, 10, 20, 50, 100, 200]


def main(n: int, coins: list) -> int:
    different_ways = [1] + [0] * n
    for coin in coins:
        for i in range(len(different_ways) - coin):
            different_ways[i + coin] += different_ways[i]
    return different_ways[-1]


def solution() -> int:
    return main(200, ALL_COINS)


if __name__ == "__main__":
    print(f"{main(5, ALL_COINS)} => {main(5, ALL_COINS) == 4}")
    print(f"{main(200, ALL_COINS)}")
