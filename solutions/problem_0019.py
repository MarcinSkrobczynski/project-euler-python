# Solution to Project Euler Problem #19: Counting Sundays
# Copyright (c) MarcinSkrobczynski

from datetime import date

import datedelta

START_TEST = date(1900, 1, 1)
END_TEST = date(1900, 12, 31)

START_DATE = date(1901, 1, 1)
END_DATE = date(2000, 12, 31)


def main(start: date, end: date):
    counter = 0
    it_date = start - datedelta.DAY
    while it_date != end:
        it_date += datedelta.DAY
        if it_date.day != 1:
            continue
        if it_date.weekday() == 6:
            counter += 1
    return counter


def solution():
    return main(START_DATE, END_DATE)


if __name__ == "__main__":
    # 01Jan1900 is Mon, 01Feb1900 is Thu, 01Mar1900 is Thu, 01Apr1900 is Sun, 01May1900 is Tue, 01Jun1900 is Fri
    # 01Jul1900 is Sun, 01Aug1900 is Wed, 01Sep1900 is Sat, 01Oct1900 is Mon, 01Nov1900 is Thu, 01Dec1900 is Sat
    print(f"{main(START_TEST, END_TEST)} => {main(START_TEST, END_TEST) == 2}")
    print(f"{main(START_DATE, END_DATE)}")
