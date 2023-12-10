import re


def day2part1(a_string: str):
    a_list = re.findall('\d+', a_string)
    dimension = 3
    composite_list = [a_list[x:x+dimension] for x in range(0, len(a_list), dimension)]
    total_wrapped_area = 0

    for rank, sub_list in enumerate(composite_list):
        l = int(sub_list[0])
        w = int(sub_list[1])
        h = int(sub_list[2])
        wrapped_area = 2*l*w + 2*w*h + 2*h*l

        area_list = [l * w, w * h, h * l]
        smallest = sorted(set(area_list))[0]
        if rank == 0:
            total_wrapped_area = wrapped_area + smallest
            continue
        total_wrapped_area += wrapped_area + smallest

    return total_wrapped_area
