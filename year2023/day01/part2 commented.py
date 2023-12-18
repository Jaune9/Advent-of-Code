from .part1 import get_sum_of_first_and_last_number_of_each_line


def day01_part2_func(code: str) -> int:
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
