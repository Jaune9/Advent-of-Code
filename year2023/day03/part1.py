"""
The idea here is to find each block of numbers and do a box around it

XXXXX
X123X
XXXXX

If our number is 123, we have to check all the X cells to see what they have.
I intended on doing the opposing (finding numbers from symbols) and failed, see "part1 first try yada yada.py"
"""
import re


def get_value_if_neighbour(matrix, number, position):
    matrix_length = len(matrix)
    line_length = matrix.find("\n")
    number_length = len(number)
    is_first_row = position < number_length
    is_last_row = position + number_length > matrix_length
    is_first_in_line = position % line_length == 0
    # is_last_in_line = (position + number_length) % (line_length + 1) == line_length
    is_last_in_line = (
        True
        if matrix_length > position + number_length
        and matrix[position + number_length] == "\n"
        else False
    )

    print(number, is_last_in_line)
    # Todo replace by a match case, see example of match later in this file
    neighbours = []
    return 0

    # Top row
    # if not is_first_row and not is_first_in_line:
    #     # above and before
    #     neighbours.append(Cell(x - 1, y - 1, matrix[y - 1][x - 1]))
    # if not is_first_row:
    #     # above
    #     neighbours.append(Cell(x, y - 1, matrix[y - 1][x]))
    # if not is_first_row and not is_last_in_line:
    #     # above and after
    #     neighbours.append(Cell(x + 1, y - 1, matrix[y - 1][x + 1]))
    #
    # # Middle row
    # if not is_first_in_line:
    #     # before
    #     neighbours.append(Cell(x - 1, y, matrix[y][x - 1]))
    # # self exist here
    # if not is_last_in_line:
    #     # after
    #     neighbours.append(Cell(x + 1, y, matrix[y][x + 1]))
    #
    # # Bottom row
    # if not is_last_row and not is_first_in_line:
    #     # below and before
    #     neighbours.append(Cell(x - 1, y + 1, matrix[y + 1][x - 1]))
    # if not is_last_row:
    #     # below
    #     neighbours.append(Cell(x, y + 1, matrix[y + 1][x]))
    # if not is_last_row and not is_last_in_line:
    #     # below and after
    #     neighbours.append(Cell(x + 1, y + 1, matrix[y + 1][x + 1]))
    # for neighbour in neighbours:
    #     if neighbour != "." and not neighbour.isnumeric():
    #         return number


# from https://stackoverflow.com/questions/4664850/how-to-find-all-occurrences-of-a-substring
def find_all(sub, a_str):
    start = 0
    while True:
        start = a_str.find(sub, start)
        if start == -1:
            return
        yield start
        start += len(sub)  # use start += 1 to find overlapping matches


def day3part1(schematics: str):
    """
    Not finished
    Issue with getting each number only once
    """
    return 0

    result = 0
    number_list = [number for number in re.findall("\d*", schematics) if number]

    number_positions = {}
    for number in number_list:
        # print(number)
        number_positions[number] = [match for match in find_all(number, schematics)]
    for number, positions in number_positions.items():
        for position in positions:
            # print(position, number)
            result += get_value_if_neighbour(schematics, number, position)
    # print(number_positions)

    return result
