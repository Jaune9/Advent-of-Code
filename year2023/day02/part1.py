import re

max_red = 12
max_green = 13
max_blue = 14


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
            if group[1] == "red":
                red = int(group[0]) if int(group[0]) > red else red
            if group[1] == "green":
                green = int(group[0]) if int(group[0]) > green else green
            if group[1] == "blue":
                blue = int(group[0]) if int(group[0]) > blue else blue
        red_ok = red <= max_red
        green_ok = green <= max_green
        blue_ok = blue <= max_blue
        sum_of_ids += red_ok and green_ok and blue_ok and int(game_number[0]) or 0
    return sum_of_ids
