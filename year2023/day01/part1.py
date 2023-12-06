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
