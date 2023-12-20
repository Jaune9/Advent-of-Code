
# partir d'un truc genre ça mais avec les diagonales
def get_adjacent_indices(i, j, m, n):
   adjacent_indices = []
    if i > 0:
        adjacent_indices.append((i-1,j))
    if i+1 < m:
        adjacent_indices.append((i+1,j))
    if j > 0:
        adjacent_indices.append((i,j-1))
    if j+1 < n:
        adjacent_indices.append((i,j+1))
    return adjacent_indices

# donc quelque chose comme ça ? (remplacer les i j par x y, please)
def get_adjacent_or_diagonal_content(i, j, row_count, line_lenght):
    near_elements = []
    is_first_row = i == 0
    is_last_row = i == row_count - 1
    is_first_in_line = j == 0
    is_last_in_line = j == line_length - 1

    # tenter un match ?

    if not is_first_row and not is_first_in_line:
      # above and before
      near_elements.append((i-1,j-1))
    if not is_first_row:
      # above
        near_elements.append((i-1,j))
    if not is_first_row and not is_last_in_line:
      # above and after
        near_elements.append((i-1,j+1))
    if not is_first_in_line:
      # before
        near_elements.append((i,j-1))
      # self exist here  
      if not is_last_in_line:
      # after
        near_elements.append((i,j+1))
      if not is_last_row and not is_first_in_line:
            # below and before
              near_elements.append((i+1,j-1))      
      if not is_last_row:
            # below
              near_elements.append((i+1,j))
        if not is_last_row and not is_last_in_line:
            # below and after
              near_elements.append((i+1,j+1))
    return near_elements
