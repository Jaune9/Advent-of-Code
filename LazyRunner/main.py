from typing import List

from Day import *


def pretty_print(days_list: List[DayPart]):
    print(days_list[0].type)
    print("                 Expected - - - - Produced")
    for day in days_list:
        print(
            f"Day {day.day} | Part {day.part} | {day.expected: >8} - - - - {day.algo(day.arg):<8}"
        )
    print("")


def print_only_one(day: int, part: int, days_list: List[DayPart]):
    pretty_print([d for d in days_list if d.day == day and d.part == part])


if __name__ == "__main__":
    print_only_one(1, 2, days_demo)
    print_only_one(1, 2, days_real)
    # pretty_print(days_demo)
    # pretty_print(days_real)
