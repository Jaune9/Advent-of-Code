import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


def get_sum_of_game_pocket_ids(game_sets: str) -> int:
    sum_of_ids = 0
    lines = game_sets.split("\n")
    for line in lines:
        if not line:
            continue
        game_number = re.search("^\w* (\d*)", line).groups()
        line = line[line.index(":") + 2 :]
        current_groups = re.findall("(\d*) (\w*)(,?;? ?)", line)
        red, green, blue = 0, 0, 0
        for group in current_groups:
            val = int(group[0])
            color = group[1]
            if color == "red":
                red = val if val > red else red
            if color == "green":
                green = val if val > green else green
            if color == "blue":
                blue = val if val > blue else blue
        red_ok = red <= MAX_RED
        green_ok = green <= MAX_GREEN
        blue_ok = blue <= MAX_BLUE
        sum_of_ids += red_ok and green_ok and blue_ok and int(game_number[0]) or 0
    return sum_of_ids
