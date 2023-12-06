from typing import List

from init2015 import *
from init2023 import *


def pretty_print(days_list: List[DayPart]):
    print(f"{days_list[0].year} - {days_list[0].type}")
    print("                 Expected - - - - Produced")
    for day in days_list:
        print(
            f"Day {day.day} | Part {day.part} | {day.expected: >8} - - - - {day.algo(day.arg):<8}"
        )
    print("")


def print_only_one(day: int, part: int, days_list: List[DayPart]):
    pretty_print([d for d in days_list if d.day == day and d.part == part])


if __name__ == "__main__":
    print_only_one(1, 2, demo_2023)
    print_only_one(1, 2, real_2023)
    pretty_print(demo_2023)
    pretty_print(real_2023)
    pretty_print(real_2015)