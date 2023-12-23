# Dataclass is really cool: you don't have to make a __init__ to have a Constructor method now
from dataclasses import dataclass


@dataclass
class Day:
    year: int
    day: int
    part: int
    type: str
    algo: callable
    arg: str
    expected: any
    result: any = None
    comment: str = ""

    def get_result(self) -> int:
        """
        Calcul the result of a day based on its algo and argument
        :return:
        """
        if not self.result:
            self.result = self.algo(self.arg)
        return self.result

    def __str__(self):
        return str(self.get_result())
