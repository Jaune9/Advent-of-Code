from pathlib import Path

demo1 = """+1 
            -1"""
demo2 = """+3 
            +3
            +4
            -2
            -4"""
demo3 = """-6 
            +3
            +8
            +5
            -6"""
demo4 = """+7
            +7
            -2
            -7
            -4"""


def part2(int_lines, frequency, past_frequencies):
    for integer in int_lines:
        frequency += integer
        if frequency in past_frequencies:
            return frequency
        past_frequencies.append(frequency)
    return part2(int_lines, frequency, past_frequencies)


def day1part2(val):
    lines = val.splitlines()
    # lines = [+1, -2, +3, +1]
    int_lines = [int(x) for x in lines]
    frequency = 0
    past_frequencies = [0]
    return part2(int_lines, frequency, past_frequencies)


if __name__ == "__main__":
    val = Path("../../arguments/2018/day01_real").read_text()

    print(demo1.splitlines())
    print(day1part2(demo1))
    print(demo2.splitlines())
    print(day1part2(demo2))
    print(demo3.splitlines())
    print(day1part2(demo3))
    print(demo4.splitlines())
    print(day1part2(demo4))

    print(day1part2(val))
