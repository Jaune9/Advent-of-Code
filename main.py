# inspect allows a fun thing, see the function "get_calling_function_name"
import inspect

# Typing is optional in Python, but recommended, as it makes following your logic easier (even to yourself)
# It also makes the IDE better at assisting you
from typing import List

# This is the class Day, that will allow us to create Day object
from Day import Day

# This is where the different parts of a day (part number, algo, input) are turned into a Day object
from init2015 import real_2015
from init2016 import real_2016
from init2023 import real_2023, demo_2023

# Just exist so black does not delete the imports above when I use them
existing_list = [real_2015, real_2016, real_2023, demo_2023]

# Different colors we can use to color our outputs
GREEN = "\033[92m"
CYAN = "\033[96m"
BLUE = "\033[94m"
YELLOW = "\033[93m"
RED = "\033[91m"
Black = "\033[30m"
White = "\033[97m"
GRAY_LIGHT = "\033[37m"
GRAY_DARK = "\033[90m"
# You can also color the background
BackgroundLightGray = "\033[47m"
BACKGROUND_GRAY_DARK = "\033[100m"
# Or change things like bold/underline and so on
BOLD = "\033[1m"
# This one is special: you put it after a color code to finish it
END_COLOR = "\033[0m"


def color_string(message: str, color_code=BLUE) -> str:
    """
    Returns our message with the associated color of the color code
    You can even add the color code together, like BACKGROUND_GRAY_DARK + BOLD below
    :param message:
    :param color_code:
    :return:
    """
    return color_code + str(message) + END_COLOR


def get_calling_function_name() -> str:
    """
    Returns the caller of the function who called it, from the stack trace
    You can not test it in the Python Console, as it relies on the Stack Trace

    ex: main(side(get_calling_function_name) == "side"
    :return:
    """
    return inspect.stack()[2][3]


def pretty_print(days_list: List[Day]) -> None:
    """
    Prints each element of a Day object list one by one with colors and their own function results.
    :param days_list:
    :return:
    """
    print(f"{days_list[0].year} - {days_list[0].type}")
    print("            Expected - - - - Produced | Valid ?")
    for day in days_list:
        # In case of a list of Days: Color even days to make the results more readable
        # In case of a "print_only_one": color the line to highlight it
        main_color = CYAN
        if get_calling_function_name() != "print_only_one":
            # A ternary operation with a first syntax
            main_color = GRAY_LIGHT if day.day % 2 == 0 else ""

        day_print = f"Day {day.day} {day.part}/2 | "
        # Below is a ternary operation. There is different models and use case for those
        day_result_color = (
            day.day % 2 == 1
            and BACKGROUND_GRAY_DARK + White + BOLD
            or BackgroundLightGray + Black + BOLD
        )
        result = day.algo(day.arg)
        day_result = color_string(
            f"{day.expected:>8} - - - - {result:<8}", day_result_color
        )

        # Compare expected/actual values to see if you keep the same result, for refactoring purposed
        message, message_color = day.expected == result and ("V", GREEN) or ("X", RED)
        day_validation = color_string(message, message_color)
        if day.comment:
            day_validation += f"  --  {day.comment}"

        # Printing the sum of the previous part, together
        print(color_string(day_print, main_color) + day_result + " | " + day_validation)
    print("")


def print_only_one(day: int, part: int, days_list: List[Day]):
    # Notion name: List comprehension
    pretty_print([d for d in days_list if d.day == day and d.part == part])


if __name__ == "__main__":
    """
    Start of the main process.
    See examples belows.
    """
    print_only_one(1, 2, demo_2023)
    print_only_one(1, 2, real_2023)
    pretty_print(demo_2023)
    pretty_print(real_2023)

    # Pick one or more
    # pretty_print(real_2015)
    # pretty_print(real_2016)
