def get_sum_of_first_and_last_number_of_each_line(code: str) -> int:
    lines = code.split('\n')
    result = 0
    for line in lines:
        current = ''
        r_line = reversed(line)
        get_first_number = lambda word: [letter for letter in word if '0' <= letter <= '9'][0]
        current += get_first_number(line) + get_first_number(r_line)
        if current:
            result += int(current)
    return result
