import importlib
import os

ANSWERS = {
    1: 233168,
    2: 4613732,
    3: 6857,
    4: 906609,
    5: 232792560,
    6: 25164150,
    7: 104743,
    8: 23514624000,
    9: 31875000,
    10: 142913828922,
    11: 70600674,
    12: 76576500,
    13: 5537376230,
    14: 837799,
    15: 137846528820,
    16: 1366,
    17: 21124,
    18: 1074,
    19: 171,
    20: 648,
}


def main():
    for i in sorted(ANSWERS.keys()):
        filename = "problem_{:04d}".format(i)
        if filename.startswith("__") or filename.startswith("utils"):
            continue
        filename = os.path.splitext(filename)[0]
        print(f"{filename}".upper())

        module = importlib.import_module(f"solutions.{filename}")
        try:
            ans = module.solution()
            if ans != ANSWERS[i]:
                print("---FAIL---")
        except AttributeError:
            print("---ERROR---")


if __name__ == "__main__":
    main()
