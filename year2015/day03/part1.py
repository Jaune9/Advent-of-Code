def day3part1(elf_orders: str):
    coords = [0, 0]
    coord_list = ["0, 0"]
    for order in elf_orders:
        if order == ">":
            coords[0] += 1
        if order == "<":
            coords[0] -= 1
        if order == "^":
            coords[1] += 1
        if order == "v":
            coords[1] -= 1
        coord_list.append(str(coords[0]) + ", " + str(coords[1]))

    return len(set(coord_list))
