from pathlib import Path

from Day import *
from year2015 import day01

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


demo_2015 = [

]

real_2015 = [
    Day1Part1Real,
    Day1Part2Real,
]
