from pathlib import Path
from pprint import pprint

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

print("Part 1 answer : ", "Power consumption == ", power_consumption)
