def split_list_into_two_columns(lines: list[str]):
    left_column = []
    right_column = []
    print(lines)
    for line in lines:
        left, right = line.split()
        left_column.append(int(left))
        right_column.append(int(right))
    return left_column, right_column

def get_sum_of_smallest_distances(code: str):
    lines = code.split("\n")
    left_column, right_column = split_list_into_two_columns(lines)

    ordered_left_column = sorted(left_column)
    ordered_right_column = sorted(right_column)

    differences = []
    for left, right in zip(ordered_left_column, ordered_right_column):
        differences.append(abs(left - right))

    sum_of_differences = sum(differences)
    return sum_of_differences
