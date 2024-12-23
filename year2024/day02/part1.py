def are_level_ordered(report: list[int]):
    ...

def are_adjacent_levels_just_different_enough():
    ...

def get_safe_report_count(code: str):
    report_list = code.split("\n")

    for report in report_list:
        int_levels = [int(level) for level in report.split()]
        print(int_levels)

    return "nope"