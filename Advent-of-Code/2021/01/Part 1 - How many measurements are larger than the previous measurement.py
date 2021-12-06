from pathlib import Path

if __name__ == "__main__":
    # parsing
    a_string = Path("input.txt").read_text()
    a_list = a_string.split()
    a_map = map(int, a_list)
    a_list_of_integers = list(a_map)

    # treatment
    larger_than_previous = 0
    for i, number in enumerate(a_list_of_integers):
        if i != 0:
            if previous < number:
                larger_than_previous += 1
        previous = number

    print("answer       :  ", larger_than_previous)
