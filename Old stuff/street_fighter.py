fighters = [
    ["Ryu", "E.Honda", "Blanka", "Guile", "Balrog", "Vega"],
    ["Ken", "Chun Li", "Zangief", "Dhalsim", "Sagat", "M.Bison"]
]
opts = ["up", "down", "right", "left"]
initial_position = (0, 0)


def test(moves, solution):
    res = street_fighter_selection(fighters, initial_position, moves)
    print(res)
    print(solution)


def street_fighter_selection(fighters, initial_position, moves):
    result = []
    i = initial_position[0]
    j = initial_position[1]
    for m in moves:
        if m == opts[2]:
            # print("{} : {} - {}".format(opts[2], i, j))
            i = 0 if i == len(fighters[j]) - 1 else i + 1
        if m == opts[3]:
            # print("{} : {} - {}".format(opts[3], i, j))
            i = len(fighters[j]) - 1 if i == 0 else i - 1
        if m == opts[1]:
            # print("{} : {} - {}".format(opts[1], i, j))
            if j != len(fighters) - 1: j += 1
        if m == opts[0]:
            # print("{} : {} - {}".format(opts[0], i, j))
            if j != 0: j -= 1
        """
        Solution for "Going up while on row 0 puts you in the last row, same index"
        if m == opts[1]:
            #print("{} : {} - {}".format(opts[1], i, j))
            j = 0 if j == len(fighters) - 1 else j + 1
        if m == opts[0]:
            #print("{} : {} - {}".format(opts[0], i, j))
            j = len(fighters) - 1 if j == 0 else j - 1
        """
        # print("result : {}\n{} - {}".format(result, i, j))
        result.append(fighters[j][i])
    return result


moves = ["left"] * 8
solution = ['Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Vega', 'Balrog']
test(moves, solution)

moves = ["right"] * 8
solution = ['E.Honda', 'Blanka', 'Guile', 'Balrog', 'Vega', 'Ryu', 'E.Honda', 'Blanka']
test(moves, solution)

moves = ["up"] * 4
solution = ['Ryu', 'Ryu', 'Ryu', 'Ryu']
test(moves, solution)

moves = ["down"] * 4
solution = ['Ken', 'Ken', 'Ken', 'Ken']
test(moves, solution)

moves = ["down", "right", "up", "left"] * 2
solution = ['Ken', 'Chun Li', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'E.Honda', 'Ryu']
test(moves, solution)

moves = ["up", "left", "down", "right"] * 2
solution = ['Ryu', 'Vega', 'M.Bison', 'Ken', 'Ryu', 'Vega', 'M.Bison', 'Ken']
test(moves, solution)

moves = ["up"] + ["left"] * 6 + ["down"] + ["right"] * 6
solution = ['Ryu', 'Vega', 'Balrog', 'Guile', 'Blanka', 'E.Honda', 'Ryu', 'Ken', 'Chun Li', 'Zangief', 'Dhalsim',
            'Sagat', 'M.Bison', 'Ken']
test(moves, solution)
