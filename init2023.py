from pathlib import Path

from Day import *
from year2023 import day01

year = 2023

Day1Part1Demo = Day(
    year=year,
    day=1,
    part=1,
    type="Demo",
    algo=day01.part1.get_sum_of_first_and_last_number_of_each_line,
    arg=Path("arguments/2023/day01_part1_demo").read_text(),
    expected=142,
)

Day1Part1Real = Day(
    year=year,
    day=1,
    part=1,
    type="Real",
    algo=day01.part1.get_sum_of_first_and_last_number_of_each_line,
    arg=Path("arguments/2023/day01_real").read_text(),
    expected=54951,
)

Day1Part2Demo = Day(
    year=year,
    day=1,
    part=2,
    type="Demo",
    algo=day01.part2.day01_part2_func,
    arg=Path("arguments/2023/day01_part2_demo").read_text(),
    expected=281,
)

Day1Part2Real = Day(
    year=year,
    day=1,
    part=2,
    type="Real",
    algo=day01.part2.day01_part2_func,
    arg=Path("arguments/2023/day01_real").read_text(),
    expected=55218,
)

demo_2023 = [
    Day1Part1Demo,
    Day1Part2Demo,
]

real_2023 = [
    Day1Part1Real,
    Day1Part2Real,
]
