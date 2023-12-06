from pathlib import Path

directions = Path("input.txt").read_text()
directions = directions.split('\n')

# test values to follow the example given there https://adventofcode.com/2021/day/2
# directions = ['f 5', 'd 5', 'f 8', 'u 3', 'd 8', 'f 2']

depth = 0
horizontal_position = 0
aim = 0

for direction in directions:
    if direction == '':
        break

    first_char = direction[0]
    value = int(direction[-1])

    if first_char == 'f':
        horizontal_position += value
        depth += aim * value

    if first_char == 'd':
        # depth += value
        aim += value
    if first_char == 'u':
        # depth -= value
        aim -= value

print(depth * horizontal_position)
