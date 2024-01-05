# just added a line to part1, make it a bool for part1


def day4part2(val):
    score = 0
    lines = val.splitlines()
    for line in lines:
        score_increase = 1
        words = [x for x in line.split()]
        if len(words) == 0:
            continue
        words = ["".join(sorted(x)) for x in words]
        counter = {x: words.count(x) for x in words}
        print(counter)
        for key, value in counter.items():
            if value > 1:
                score_increase = 0
        score += score_increase

    return score
