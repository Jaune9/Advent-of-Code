"""
/!\ Unfinished /!\
"""

tests = [(1, 0), (12, 3), (23, 2), (1024, 31)]

val = """277678"""


def day2part3(score):
    if score == 1:
        return "none", 0, -1, -1
    if score in [2, 4, 6, 8]:
        return "none", 1, -1, -1
    if score in [3, 5, 7, 9]:
        return "none", 2, -1, -1
    grid = 1
    iterator = 1
    while score > grid:
        grid = grid + iterator
        if score <= grid:
            # alors score est en bas
            return "down", score, grid, iterator
        grid = grid + iterator
        if score <= grid:
            # alors score est à droite
            return "right", score, grid, iterator
        iterator += 1

        grid = grid + iterator
        if score <= grid:
            # alors score est en haut
            return "up", score, grid, iterator
        grid = grid + iterator
        if score <= grid:
            # alors score est à gauche
            return "left", score, grid, iterator
        iterator += 1


def meh(direction, score, grid, iterator):
    print(direction, score, grid, iterator)
    if direction == "none":
        return score
    layers_count = iterator - 2
    layer_width = 2 * iterator + 1
    if score == grid:
        print("idunnoshit", score, iterator)
        return layers_count + layer_width


"""
Big idea:
From the start, you do 
+1 to the right 
+1 to the top 
+2 to the left 
+2 to the bottom 
+3 to the right 
+3 to the top 
and so on. 
So we can find the "layer" the number we are looking for is at + direction from this
alls rows are even so len(row)/2 == x.5, x+1 == the middle
from this + iterator we can get our number position
"""

if __name__ == "__main__":
    for test in tests:
        direction, score, grid, iterator = day2part3(int(test[0]))
        print(meh(direction, score, grid, iterator))
    for i in range(1, 25):
        print(day2part3(i))
        direction, score, grid, iterator = day2part3(i)
        print(meh(direction, score, grid, iterator))

    print(day2part3(int(val)))
