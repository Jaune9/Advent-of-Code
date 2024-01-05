tests = [("5\t1\t9\t5", 8), ("7\t5\t3", 4), ("2\t4\t6\t8", 6)]


def day2part1_process(string):
    min = 9999999999999999999999999999
    max = 0
    number_string = string.split("\t")
    for n in number_string:
        n = int(n)
        min = n if n < min else min
        max = n if n > max else max
    return max - min


def day2part1(val):
    # for test in tests:
    #     print(day2part1(test[0]), f"expected {test[1]}")
    lines = val.split("\n")
    res = 0
    for line in lines:
        res += day2part1(line)
    return res
