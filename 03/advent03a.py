import numpy


def load_file(file):
    with open(file, encoding="utf-8") as file:
        all_lines = [line.strip() for line in file.readlines()]
    return all_lines


def most_common_values(list):

    values = []
    for i in range(len(list[0])):
        new_list = [num[i] for num in list]
        if new_list.count("0") > new_list.count("1"):
            values.append("0")
        else:
            values.append("1")
    return values


def convert_bin_string_to_decimal(value):
    number = "".join(value)
    return int(number, 2)


def reverse_most_common_values(values):
    new_values = []
    for char in values:
        new_values.append("0") if char == "1" else new_values.append("1")
    return new_values


def multiply_numbers(numbers):
    return numpy.prod(numbers)


binary_list = load_file("binary_a.txt")
gamma = convert_bin_string_to_decimal(most_common_values(binary_list))
epsilon = convert_bin_string_to_decimal(
    reverse_most_common_values(most_common_values(binary_list))
)
result = multiply_numbers([gamma, epsilon])
