from pathlib import Path

from Day import *
from year2016 import day01

year = 2016

Day1Real = Day(
    year=2016,
    day=1,
    part=1,
    type="Real",
    algo=day01.part1.day1code,
    arg=Path("arguments/2016/day01_real").read_text(),
    expected=246,
)


demo_2016 = []

real_2016 = [
    Day1Real,
]
