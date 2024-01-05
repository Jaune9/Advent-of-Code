tests = [("1122", 3), ("1111", 4), ("1234", 0), ("91212129", 9)]


def day1part1(string):
    res = 0
    for index, char in enumerate(string):
        if index < len(string) - 1:
            if char == string[index + 1]:
                res += int(char)
        if index == len(string) - 1:
            if char == string[0]:
                res += int(char)
    return res


if __name__ == "__main__":
    for test in tests:
        print(day1part1(test[0]), f"expected {test[1]}")
