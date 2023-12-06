from dataclasses import dataclass


@dataclass
class DayPart:
    year: int
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
