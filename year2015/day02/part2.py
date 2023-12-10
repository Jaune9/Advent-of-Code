import re


def day2part2(a_string: str):
    a_list = re.findall('\d+', a_string)
    dimension = 3
    composite_list = [a_list[x:x+dimension] for x in range(0, len(a_list), dimension)]
    total_wrapped_area = 0
    total_ribbon_length = 0

    for rank, sub_list in enumerate(composite_list):
        l = int(sub_list[0])
        w = int(sub_list[1])
        h = int(sub_list[2])
        wrapped_area = 2*l*w + 2*w*h + 2*h*l

        area_list = [l * w, w * h, h * l]
        smallest_section = sorted(area_list)[0]

        # part 2 :
        ribbon_length = 2 * min(l+w, w+h, h+l)
        ribbon_length += l * w * h

        if rank == 0:
            total_wrapped_area = wrapped_area + smallest_section
            total_ribbon_length = ribbon_length
            continue
        total_wrapped_area += wrapped_area + smallest_section
        total_ribbon_length += ribbon_length

    return total_ribbon_length
