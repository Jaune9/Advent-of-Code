import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_total_power(game_sets: str) -> int:
    total_power = 0
    lines = game_sets.split("\n")
    for line in lines:
        if not line:
            continue
        line = line[line.index(":") + 2 :]
        current_groups = re.findall("(\d*) (\w*)(,?;? ?)", line)
        red, green, blue, line_power = 0, 0, 0, 0
        for group in current_groups:
            val = int(group[0])
            color = group[1]
            separator = group[2]
            if color == "red":
                red = val if val > red else red
            if color == "green":
                green = val if val > green else green
            if color == "blue":
                blue = val if val > blue else blue
            if separator in ["", "; "]:
                red = red if red > 0 else 1
                green = green if green > 0 else 1
                blue = blue if blue > 0 else 1
                group_power = red * green * blue
                line_power = group_power if group_power > line_power else line_power
        total_power += line_power
    return total_power
