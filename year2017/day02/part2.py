tests = [("5\t1\t9\t5", 8), ("7\t5\t3", 4), ("2\t4\t6\t8", 6)]


def day2part2_process(string):
    number_string = string.split("\t")
    for n in number_string:
        n = int(n)
        for n2 in number_string:
            n2 = int(n2)
            if n == n2:
                continue
            if n % n2 == 0:
                return n // n2
            if n2 % n == 0:
                return n2 // n


def day2part2(val):
    # for test in tests:
    #     print(day2part1(test[0]), f"expected {test[1]}")
    lines = val.split("\n")
    res = 0
    for line in lines:
        res += day2part2_process(line)
    return res
