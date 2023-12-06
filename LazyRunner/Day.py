from dataclasses import dataclass

from arguments import *
from day01 import *


@dataclass
class DayPart:
    day: int
    part: int
    type: str
    algo: callable
    arg: str
    expected: any
    result: any = None

    def get_result(self):
        if not self.result:
            self.result = self.algo(self.arg)
        return self.result

    def __str__(self):
        return str(self.get_result())


Day1Part1Demo = DayPart(
    day=1,
    part=1,
    type="Demo",
    algo=day01.get_sum_of_first_and_last_number_of_each_line,
    arg=day01_part1_demo_arg,
    expected=142,
)

Day1Part1Real = DayPart(
    day=1,
    part=1,
    type="Real",
    algo=day01.get_sum_of_first_and_last_number_of_each_line,
    arg=day01_real_arg,
    expected=54951,
)

Day1Part2Demo = DayPart(
    day=1,
    part=2,
    type="Demo",
    algo=day01.day01_part2_func,
    arg=day01_part2_demo_arg,
    expected=281,
)

Day1Part2Real = DayPart(
    day=1,
    part=2,
    type="Real",
    algo=day01.day01_part2_func,
    arg=day01_real_arg,
    expected=55218,
)

days_demo = [
    Day1Part1Demo,
    Day1Part2Demo,
]

days_real = [
    Day1Part1Real,
    Day1Part2Real,
]
