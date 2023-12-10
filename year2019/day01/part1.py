from pathlib import Path


def input_parser(input_to_parse):
    inputstr = Path(input_to_parse).read_text()
    inputstrlist = inputstr.split()
    parsed_input = [int(x) for x in inputstrlist]
    return parsed_input


def recursive_full_calc(fuel_amount: int):
    if fuel_amount <= 0:
        return 0
    return fuel_amount + recursive_full_calc(fuel_amount // 3 - 2)


def ex01(mass_list):
    fuel = 0
    added_full = 0
    for mass in mass_list:
        # fuel = 0  # test
        current_fuel = mass // 3 - 2
        fuel += current_fuel
        added_full += recursive_full_calc(current_fuel)
        # print(fuel)

    return fuel, added_full


def test_default_value():
    mass_list_example = [12, 14, 1969, 100756]
    """
    For a mass of 12, divide by 3 and round down to get 4, then subtract 2 to get 2.
    For a mass of 14, dividing by 3 and rounding down still yields 4, so the fuel required is also 2.
    For a mass of 1969, the fuel required is 654.
    For a mass of 100756, the fuel required is 33583.
    """
    ex01(mass_list_example)


if __name__ == "__main__":
    print(ex01(input_parser("2019input01")))
