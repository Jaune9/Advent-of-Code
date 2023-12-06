def count_parenthesis_safely(a_string):

    opened = 0
    closed = 0
    for position, character in enumerate(a_string):
        position += 1
        if character == '(':
            opened += 1
        if character == ')':
            closed += 1

        if opened - closed < 0:
            return position

    return opened - closed
