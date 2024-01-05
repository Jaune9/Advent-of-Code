tests = [("1212", 6), ("1221", 0), ("123425", 4), ("123123", 12), ("12131415", 4)]


def day1part2(string):
    res = 0
    step = len(string) // 2
    for index, char in enumerate(string):
        if index < len(string) - 1 - step:
            if char == string[index + step]:
                res += int(char)
        elif char == string[index - step]:
            res += int(char)
    return res


if __name__ == "__main__":
    for test in tests:
        print(day1part2(test[0]), f"expected {test[1]}")
