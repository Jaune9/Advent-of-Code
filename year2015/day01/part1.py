def count_parenthesis(a_string):
    opened = 0
    closed = 0
    for character in a_string:
        if character == '(':
            opened += 1
        if character == ')':
            closed += 1

    return opened - closed
