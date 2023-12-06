from pathlib import Path

directions = Path("input.txt").read_text()
directions = directions.split('\n')

depth = 0
horizontal_position = 0

for direction in directions:
    if direction == '':
        break

    first_char = direction[0]
    value = int(direction[-1])

    if first_char == 'f':
        horizontal_position += value

    if first_char == 'd':
        depth += value
    if first_char == 'u':
        depth -= value

print(depth * horizontal_position)
