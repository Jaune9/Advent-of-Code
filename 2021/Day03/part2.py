from pathlib import Path


def recursive_bit_search_most_common(bit_list, column):
    ones = 0
    ones_list = []
    zeroes = 0
    zeroes_list = []
    for bit in bit_list:
        if bit == '':
            break
        if bit[column] == '1':
            ones += 1
            ones_list.append(bit)
        else:
            zeroes += 1
            zeroes_list.append(bit)
    if ones < zeroes:
        if zeroes == 1:
            return zeroes_list[0]
        return recursive_bit_search_most_common(zeroes_list, column + 1)
    if ones in [0, 1]:
        return ones_list[0]
    return recursive_bit_search_most_common(ones_list, column + 1)


def recursive_bit_search_least_common(bit_list, column):
    ones = 0
    ones_list = []
    zeroes = 0
    zeroes_list = []
    for bit in bit_list:
        if bit == '':
            break
        if bit[column] == '1':
            ones += 1
            ones_list.append(bit)
        else:
            zeroes += 1
            zeroes_list.append(bit)
    if ones > zeroes:
        if zeroes == 1:
            return zeroes_list[0]
        return recursive_bit_search_least_common(zeroes_list, column + 1)
    if ones in [0, 1]:
        return ones_list[0]
    return recursive_bit_search_least_common(ones_list, column + 1)


diagnostic_report = Path("input.txt").read_text()
diagnostic_report = diagnostic_report.split('\n')

sums_of_columns = [0] * len(diagnostic_report[0])
for index, binary_number in enumerate(diagnostic_report):
    if binary_number == '':
        break
    if index == 0:
        for i, number in enumerate(binary_number):
            sums_of_columns[i] = int(number)
        continue
    for e, num in enumerate(binary_number):
        sums_of_columns[e] = sums_of_columns[e] + int(num)

gamma_rate = [1 if x > len(diagnostic_report) // 2 else 0 for x in sums_of_columns]
epsilon_rate = [1 if x == 0 else 0 for x in gamma_rate]

# the int() cast takes the base of origine as a second argument, if any.
gamma_rate_int_value = int(''.join(str(x) for x in gamma_rate), 2)
epsilon_rate_int_value = int(''.join(str(x) for x in epsilon_rate), 2)

power_consumption = gamma_rate_int_value * epsilon_rate_int_value

oxygen_generator_rating = recursive_bit_search_most_common(diagnostic_report, 0)
C02_scrubber_rating = recursive_bit_search_least_common(diagnostic_report, 0)
life_support_rating = int(oxygen_generator_rating, 2) * int(C02_scrubber_rating, 2)

print("Part 1 answer : ", "Power consumption == ", power_consumption)
print("Part 2 answer : ", "Life support rating == ", life_support_rating)
