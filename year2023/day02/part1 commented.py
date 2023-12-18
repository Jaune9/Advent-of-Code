"""
re, or regex, are regular expression, a very powerful tool that seems totally unreadable at first
this tool https://regex101.com/ or any other will be welcome to try your hands at it
the idea is to match patterns, like "I want a word followed by a number"
so you can say "about the thing that match the pattern, give it to me in this variable"
"""
import re

max_red = 12
max_green = 13
max_blue = 14
# you should CAPITALIZE your constant, not like I did here


def get_sum_of_game_pocket_ids(game_sets: str) -> int:
    sum_of_ids = 0
    lines = game_sets.split("\n")
    for line in lines:
        """
        this is a failsafe: if a line is empty (often happens at the beginning/end of treatement)
        then you skip the line, simple as that
        A saying about this is "quit early" or "fail early", do the specific early so you can focus on the general
        """
        if not line:
            continue

        """
        a first regex. 
        ^ means "begin with"
        $ means "ends with"
        \w means a letter
        \d means a digit
        * means "as many as you want"
        () forms a group
        We can get what is in a group later, and we want the game number, so we put only the digit part in a group
        """
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
