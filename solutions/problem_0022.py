# Solution to Project Euler Problem #22: Names scores
# Copyright (c) MarcinSkrobczynski


def name_value(name: str) -> int:
    return sum(int(ord(x) - ord('A') + 1) for x in name)


def name_score(names: list, name: str) -> int:
    if name not in names:
        raise ValueError

    return (names.index(name) + 1) * name_value(name)


def get_names(filename: str) -> list:
    with open(filename, 'r') as file:
        data = file.read().replace('\n', '').replace('"', '')
    return sorted(data.split(","))


def main(filename: str) -> int:
    names = get_names(filename)
    return sum((i + 1) * (ord(x) - ord('A') + 1)
               for (i, name) in enumerate(names)
               for x in name)


def solution() -> int:
    return main('solutions/resources/22_names.txt')


if __name__ == "__main__":
    f = 'resources/22_names.txt'
    n = get_names(f)

    print(f"{name_value('COLIN')} => {name_value('COLIN') == 53}")
    print(f"{name_score(n, 'COLIN')} => {name_score(n, 'COLIN') == 49714}")
    print(f"{main('resources/22_names.txt')}")
