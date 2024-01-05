from pathlib import Path


def day1part1(val):
    lines = val.splitlines()
    # lines = [+1, -2, +3, +1]
    int_lines = [int(x) for x in lines]
    frequency = 0
    for integer in int_lines:
        frequency += integer
    return frequency


if __name__ == "__main__":
    val = Path("../../arguments/2018/day01_real").read_text()
    print(day1part1(val))
