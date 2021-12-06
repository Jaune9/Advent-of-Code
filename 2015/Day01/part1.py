from pathlib import Path

if __name__ == "__main__":

    # parsing
    a_string = Path("input.txt").read_text()

    opened = 0
    closed = 0
    for character in a_string:
        if character == '(':
            opened += 1
        if character == ')':
            closed += 1

    print("Part 1 answer : ", opened - closed)
