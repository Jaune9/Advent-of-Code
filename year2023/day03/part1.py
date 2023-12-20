def get_adjacent_or_diagonal_cells(x, y, row_count, line_length):
    near_elements = []
    is_first_row = x == 0
    is_last_row = x == row_count - 1
    is_first_in_line = y == 0
    is_last_in_line = y == line_length - 1

    # tenter un match ?

    if not is_first_row and not is_first_in_line:
        # above and before
        near_elements.append((x - 1, y - 1))
    if not is_first_row:
        # above
        near_elements.append((x - 1, y))
    if not is_first_row and not is_last_in_line:
        # above and after
        near_elements.append((x - 1, y + 1))
    if not is_first_in_line:
        # before
        near_elements.append((x, y - 1))
    # self exist here
    if not is_last_in_line:
        # after
        near_elements.append((x, y + 1))
    if not is_last_row and not is_first_in_line:
        # below and before
        near_elements.append((x + 1, y - 1))
    if not is_last_row:
        # below
        near_elements.append((x + 1, y))
    if not is_last_row and not is_last_in_line:
        # below and after
        near_elements.append((x + 1, y + 1))
    return near_elements


def get_adjacent_content(matrix, cell_x, cell_y):
    neighbours = get_adjacent_or_diagonal_cells(cell_x, cell_y, len(matrix[0]), len(matrix))
    neighbours_content = []
    for neighbour in neighbours:
        neighbours_content.append(matrix[cell_x+neighbour[0]][cell_y+neighbour[1]])
    return neighbours_content


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]
    print(get_adjacent_or_diagonal_cells(1, 1, 3, 3))
    print(get_adjacent_or_diagonal_cells(0, 0, 3, 3))
    print(get_adjacent_content(matrix, 0, 0))

