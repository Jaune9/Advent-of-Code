def treatment(an_order, coords, coord_list):
    if an_order == ">":
        coords[0] += 1
    if an_order == "<":
        coords[0] -= 1
    if an_order == "^":
        coords[1] += 1
    if an_order == "v":
        coords[1] -= 1
    coord_list.append(str(coords[0]) + ", " + str(coords[1]))


def day3part2(elf_orders: str):
    santa_coords = [0, 0]
    robot_coords = [0, 0]
    santa_coord_list = ["0, 0"]
    robot_coord_list = ["0, 0"]
    for index, order in enumerate(elf_orders):
        if index % 2 == 0:
            treatment(order, santa_coords, santa_coord_list)
        else:
            treatment(order, robot_coords, robot_coord_list)

    all_coords = santa_coord_list + robot_coord_list
    coords_amount = len(set(all_coords))
    return coords_amount
