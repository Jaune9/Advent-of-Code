from pathlib import Path
import re


if __name__ == "__main__":

    # parsing
    a_string = Path("input.txt").read_text()
    a_list = re.findall('\d+', a_string)
    dimension = 3
    composite_list = [a_list[x:x+dimension] for x in range(0, len(a_list), dimension)]

    # treatment
    for rank, sub_list in enumerate(composite_list):
        # get area covered by wrapped paper :
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

    print("Part 1 answer : ", total_wrapped_area)
