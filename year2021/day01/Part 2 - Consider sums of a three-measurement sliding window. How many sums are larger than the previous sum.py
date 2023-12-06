from pathlib import Path

if __name__ == "__main__":
    # parsing
    a_string = Path("input.txt").read_text()
    a_list = a_string.split()
    a_map = map(int, a_list)
    a_list_of_integers = list(a_map)

    # treatment
    window_size = 3
    larger_than_previous = 0
    for i in range(len(a_list_of_integers) - window_size + 1):
        # for each element in the list but the last remaining ones

        # current is the sum of the current + X next
        current = sum(a_list_of_integers[i: i + window_size])

        # if no previous, current become previous and jump to next loop
        if i == 0:
            previous = current
            continue
        else:
            larger_than_previous += 1 if current > previous else 0
            previous = current

    print("answer       :  ", larger_than_previous)
