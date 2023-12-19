"""
re, or regex, are regular expression, a very powerful tool that seems totally unreadable at first
this tool https://regex101.com/ or any other will be welcome to try your hands at it
the idea is to match patterns, like "I want a word followed by a number"
so you can say "about the thing that match the pattern, give it to me in this variable"
"""
import re

MAX_RED = 12
MAX_GREEN = 13
MAX_BLUE = 14


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
        We can get what is in a group later
        Here, we want the game number, so we put only the digit part in a group
        """
        game_number = re.search("^\w* (\d*)", line).groups()
        """
        We don't need the "Game XX :" part of the line anymore, so we cut it
        Because we don't know how long the number can be, we cut at ":" and advance by 2 to be where we want
        """
        line = line[line.index(":") + 2 :]
        """
        ? means "can be there or not"
        Here, we want the number, the color, and maybe even know when there is a ; just in case
        So we make 3 groups just for that
        """
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
        """
        here we check if everything is true between red_ok and so on. 
        if it is, we add the value. If not, we add 0 (handier than doing nothing here)
        """
        sum_of_ids += red_ok and green_ok and blue_ok and int(game_number[0]) or 0
    return sum_of_ids
