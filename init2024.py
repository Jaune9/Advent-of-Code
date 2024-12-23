from pathlib import Path

from Day import *
from year2024 import day01, day02

year = 2024

Day1Part1Demo = Day(
    year=year,
    day=1,
    part=1,
    type="Demo",
    algo=day01.part1.get_sum_of_smallest_distances,
    arg=Path("arguments/2024/day01_part1_demo").read_text(),
    expected=11,
)

Day1Part1Real = Day(
    year=year,
    day=1,
    part=1,
    type="Real",
    algo=day01.part1.get_sum_of_smallest_distances,
    arg=Path("arguments/2024/day01_part1_real").read_text(),
    expected=2164381,
)

Day1Part2Real = Day(
    year=year,
    day=1,
    part=1,
    type="Real",
    algo=day01.part2.get_similarity_score,
    arg=Path("arguments/2024/day01_part1_real").read_text(),
    expected=20719933,
)

Day2Part1Demo = Day(
    year=year,
    day=1,
    part=1,
    type="Demo",
    algo=day02.part1.get_safe_report_count,
    arg=Path("arguments/2024/day02_part1_demo").read_text(),
    expected=11,
)

demo_2024 = [
    Day1Part1Demo,
    Day2Part1Demo
]

real_2024 = [
    Day1Part1Real,
    Day1Part2Real
]
