from pathlib import Path


def update_pos(c, p):
    return_value = {
        '>': (p[0] + 1, p[1]),
        '<': (p[0] - 1, p[1]),
        '^': (p[0], p[1] + 1),
        'v': (p[0], p[1] - 1)
    }
    return return_value[c]


content = Path('input.txt').read_text()
pos = [(0, 0), (0, 0)]  # one is Santa, the other Robo-Santa
visited_houses = {(0, 0): True}
for i in range(len(content)):
    t = pos[i % 2] = update_pos(content[i], pos[i % 2])
    visited_houses[t] = True
print(len(visited_houses))
