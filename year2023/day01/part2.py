from .part1 import get_sum_of_first_and_last_number_of_each_line


def day01_part2_func(code: str) -> int:
    """
    This one might feel a little like cheating.
    Take in consideration some of the number_as_string can overlap:
    oneight is a valid line to have in the exercise and should give 18.
    If you replace one by 1, you get 1ight, so eight won't be replaced by 8 since the 'e' is missing
    Replace one by one1one prevents us from erasing either the beginning or the end of the chain
    From there, we can re-use part1.py func as it is.
    Most "days" are done in a way that encourages you to re-use part1.py in part2.py
    """
    replaced_code = (
        code.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    )
    return get_sum_of_first_and_last_number_of_each_line(replaced_code)
