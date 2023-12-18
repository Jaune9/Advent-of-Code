def get_first_number_in_str(the_string: str) -> str:
    for letter in the_string:
        if "0" <= letter <= "9":
            return letter


def get_sum_of_first_and_last_number_of_each_line(code: str) -> int:
    lines = code.split("\n")
    result = 0
    for line in lines:
        current = ""
        current += get_first_number_in_str(line) + get_first_number_in_str(line[::-1])
        if current:
            result += int(current)
    return result
