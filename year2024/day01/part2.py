from part1 import split_list_into_two_columns

def get_similarity_score(code: str):
    lines = code.split("\n")
    left_col, right_col = split_list_into_two_columns(lines)
    total_similarity_score = 0
    for line in lines:
        left, right = line.split()
        left_appearance_in_right_col = right_col.count(int(left))
        similarity_score = int(left) * left_appearance_in_right_col
        total_similarity_score += similarity_score

    return total_similarity_score