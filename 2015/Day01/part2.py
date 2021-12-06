from pathlib import Path

if __name__ == "__main__":

    # parsing
    a_string = Path("input.txt").read_text()

    opened = 0
    closed = 0
    for position, character in enumerate(a_string):
        position += 1
        if character == '(':
            opened += 1
        if character == ')':
            closed += 1

        if opened - closed < 0:
            print("Part 2 answer : ", position)
            exit("Comment lines from 15 to 17 included for Part 1 answer")

    print("Part 1 answer : ", opened - closed)
