from pathlib import Path


def day5part1(val):
    step = 0
    lines = val.splitlines()
    int_lines = [int(x) for x in lines]
    current_pos = 0
    while True:
        next_pos = current_pos + int_lines[current_pos]
        int_lines[current_pos] = int_lines[current_pos] + 1
        current_pos = next_pos
        step += 1
        if current_pos >= len(int_lines):
            break
    return step


if __name__ == "__main__":
    val = Path("../../arguments/2017/day05_real").read_text()
    print(day5part1(val))
