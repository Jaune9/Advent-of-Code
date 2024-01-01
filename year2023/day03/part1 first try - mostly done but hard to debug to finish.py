"""
We are looking for numbers adjacent to symbols 
So we are looking for numbers, right ?
But what if there are thousands and thousands of numbers and no/few symbol ?
You waste time and resources
So I suggest we look for symbol who have adjacent numbers instead

The idea is as follows:
- Get symbols positions
- Get numbers adjacent to symbols positions
- Somehow check they are not the same number I guess ?
- Get left and right neighbours of numbers who also are numbers
- Profit ??! 
"""


class Cell:
    x: int
    y: int
    content: str

    def __init__(self, x, y, char):
        self.x = x
        self.y = y
        self.content = char

    def __repr__(self):
        return f"({self.x},{self.y}):{self.content}"

    def isnumeric(self):
        return self.content.isnumeric()


def concat_int(v1: int, v2: int or None):
    """
    Add number like when you couldn't math:
    1 + 2 == 12

    If only v1 is valid, returns only v1 as recursive_get_right_number can return None
    """
    if v2 is None:
        return int(v1)
    return int(str(v1) + str(v2))


def get_neighbours(matrix, symbol: Cell):
    """
    We split the neighbours into top, middle and bottom ones for later
    Be careful about append(..., matrix[][]) value, it is matrix[y][x], not [x][y]
    """
    row_count = len(matrix)
    line_length = len(matrix[0])
    x, y = symbol.x, symbol.y
    top_row_neighbours = []
    middle_row_neighbours = []
    bottom_row_neighbours = []
    is_first_row = y == 0
    is_last_row = y == line_length - 1
    is_first_in_line = x == 0
    is_last_in_line = x == row_count - 1

    # Todo replace by a match case, see example of match later in this file

    # Top row
    if not is_first_row and not is_first_in_line:
        # above and before
        top_row_neighbours.append(Cell(x - 1, y - 1, matrix[y - 1][x - 1]))
    if not is_first_row:
        # above
        top_row_neighbours.append(Cell(x, y - 1, matrix[y - 1][x]))
    if not is_first_row and not is_last_in_line:
        # above and after
        top_row_neighbours.append(Cell(x + 1, y - 1, matrix[y - 1][x + 1]))

    # Middle row
    if not is_first_in_line:
        # before
        middle_row_neighbours.append(Cell(x - 1, y, matrix[y][x - 1]))
    # self exist here
    if not is_last_in_line:
        # after
        middle_row_neighbours.append(Cell(x + 1, y, matrix[y][x + 1]))

    # Bottom row
    if not is_last_row and not is_first_in_line:
        # below and before
        bottom_row_neighbours.append(Cell(x - 1, y + 1, matrix[y + 1][x - 1]))
    if not is_last_row:
        # below
        bottom_row_neighbours.append(Cell(x, y + 1, matrix[y + 1][x]))
    if not is_last_row and not is_last_in_line:
        # below and after
        bottom_row_neighbours.append(Cell(x + 1, y + 1, matrix[y + 1][x + 1]))
    return [top_row_neighbours, middle_row_neighbours, bottom_row_neighbours]


def get_symbols(matrix):
    positions = []
    for y, line in enumerate(matrix):
        for x, char in enumerate(line):
            if char in ["*", "+", "#", "$"]:
                positions.append(Cell(x, y, char))
    return positions


def recursive_get_left_number(neighbour, matrix, temp_x) -> int:
    """
    Ok, a lot happens here
    This is a recursive function, a function ment to call itself
    It can be more efficient than a while or for loop in some case
    Google it for a simpler example, then come back to this one later

    The idea : if we go from a number to a neighbour, it can go left or right
    If we take the very first example, 467
    Starting from 7, you go left to get the 6, then the 4
    But you can't do 7 + 6 + 4, you have to do 7 + 6 * 10 + 4 * 100
    If you started from 4, you would need to go right to the 6, then the 7
    Same, you can't do 4 + 6 + 7, you have to do 4 * 100 + 6 * 10 + 7
    Iterator also changes with the direction, as we want to go left or right, x has +1 or -1l
    """
    coefficient_current, coefficient_next = 1, 10
    iterator = -1

    if matrix[neighbour.y][temp_x].isnumeric():
        if 0 <= temp_x:
            return coefficient_current * int(
                matrix[neighbour.y][temp_x]
            ) + coefficient_next * recursive_get_left_number(
                neighbour, matrix, temp_x + iterator
            )
    return 0


def recursive_get_right_number(neighbour, matrix, temp_x) -> int or None:
    """
    Ok, a lot happens here
    This is a recursive function, a function ment to call itself
    It can be more efficient than a while or for loop in some case
    Google it for a simpler example, then come back to this one later

    The idea : if we go from a number to a neighbour, it can go left or right
    If we take the very first example, 467
    Starting from 7, you go left to get the 6, then the 4
    But you can't do 7 + 6 + 4, you have to do 7 + 6 * 10 + 4 * 100
    If you started from 4, you would need to go right to the 6, then the 7
    Same, you can't do 4 + 6 + 7, you have to do 4 * 100 + 6 * 10 + 7
    Iterator also changes with the direction, as we want to go left or right, x has +1 or -1l
    """
    print(matrix[neighbour.y], temp_x)
    print(
        "put a breakpoint here with temp_x == len(matrix[0]) and you'll see the 7 4 5 nicely that ends on x==140"
        "index out of range de mékouy",
        "faut handle le 0 en fait T___T",
    )
    print(matrix[neighbour.y][temp_x])
    if matrix[neighbour.y][temp_x].isnumeric():
        if temp_x < len(matrix[neighbour.y]):
            return concat_int(
                matrix[neighbour.y][temp_x],
                recursive_get_right_number(neighbour, matrix, temp_x + 1),
            )
    return


def get_number(neighbours, matrix):
    result = 0
    for neighbour in neighbours:
        left_value = 0
        if neighbour[0].isnumeric():
            temp_x = neighbour[0].x
            left_value = recursive_get_left_number(neighbour[0], matrix, temp_x)
        mid_value = int(neighbour[1].content) if neighbour[1].isnumeric() else 0
        right_value = 0
        if neighbour[-1].isnumeric():
            temp_x = neighbour[-1].x
            right_value = recursive_get_right_number(neighbour[-1], matrix, temp_x)

        value = 0
        match left_value, mid_value, right_value:
            case left_value, 0, 0:
                value = left_value
            case left_value, mid_value, 0:
                value = concat_int(left_value, mid_value)
            case left_value, 0, right_value:
                value = left_value + right_value
            case left_value, mid_value, right_value:
                value = concat_int(left_value, concat_int(mid_value, right_value))
            case 0, mid_value, 0:
                value = mid_value
            case 0, mid_value, right_value:
                value = concat_int(mid_value, right_value)
            case 0, 0, right_value:
                value = right_value
        print(left_value, mid_value, right_value, value)
        result += value
    return result


def day3part1(schematics: str):
    # parsing
    matrix = schematics.split("\n")

    # demo for tool functions
    symbols = get_symbols(matrix)
    result = 0
    for symbol in symbols:
        neighbours = get_neighbours(matrix, symbol)
        result += get_number(neighbours, matrix)
    return result
