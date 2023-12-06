def get_sum_of_first_and_last_number_of_each_line(code: str) -> int:
    lines = code.split('\n')
    result = 0
    for line in lines:
        current = ''
        for letter in line:
            if '0' <= letter <= '9':
                current += letter
                break
        for letter in reversed(line):
            if '0' <= letter <= '9':
                current += letter
                break
        if current:
            result += int(current)
    return result


# fixme Deprecated, works in a sense but not the other
def old_day01_part2_process(line: str, reversed_order: bool = False):
    int_as_str = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    number_index = 0
    number_value = 0
    for position, letter in enumerate(line):
        if '0' <= letter <= '9':
            number_index = position
            number_value = letter
            break
    letter_index = 9999
    letter_value = ''
    for numb in int_as_str:
        if 0 <= line.find(numb) < letter_index:
            letter_index = line.find(numb)
            letter_value = numb

    if letter_index < number_index:
        return int_as_str.index(letter_value) + 1
    return str(number_value)


def day01_part2_process(line):
    ...


def day01_part2_func(code: str) -> int:
    replaced_code = code.replace("one", "one1one").replace("two", "two2two").replace("three", "three3three").replace("four", "four4four").replace("five", "five5five").replace("six", "six6six").replace("seven", "seven7seven").replace("eight", "eight8eight").replace("nine", "nine9nine")
    lines = replaced_code.split('\n')
    result = 0
    for line in lines:
        if line == '':
            continue
        result += get_sum_of_first_and_last_number_of_each_line(line)
    return result
