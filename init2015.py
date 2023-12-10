from pathlib import Path

from Day import *
from year2015 import day01, day02, day03

Day1Part1Real = DayPart(
    year=2015,
    day=1,
    part=1,
    type="Real",
    algo=day01.part1.count_parenthesis,
    arg=Path("arguments/2015/day01_real").read_text(),
    expected=138,
)

Day1Part2Real = DayPart(
    year=2015,
    day=1,
    part=2,
    type="Real",
    algo=day01.part2.count_parenthesis_safely,
    arg=Path("arguments/2015/day01_real").read_text(),
    expected=1771,
)

Day2Part1Real = DayPart(
    year=2015,
    day=2,
    part=1,
    type="Real",
    algo=day02.part1.day2part1,
    arg=Path("arguments/2015/day02_real").read_text(),
    expected=1598415,
)

Day2Part2Real = DayPart(
    year=2015,
    day=2,
    part=2,
    type="Real",
    algo=day02.part2.day2part2,
    arg=Path("arguments/2015/day02_real").read_text(),
    expected=3812909,
)


Day3Part1Real = DayPart(
    year=2015,
    day=3,
    part=1,
    type="Real",
    algo=day03.part1.day3part1,
    arg=Path("arguments/2015/day03_real").read_text(),
    expected=2592,
)

Day3Part2Real = DayPart(
    year=2015,
    day=3,
    part=2,
    type="Real",
    algo=day03.part2.day3part2,
    arg=Path("arguments/2015/day03_real").read_text(),
    expected=2360,
)


demo_2015 = [

]

real_2015 = [
    Day1Part1Real,
    Day1Part2Real,
    Day2Part1Real,
    Day2Part2Real,
    Day3Part1Real,
    Day3Part2Real,
]
