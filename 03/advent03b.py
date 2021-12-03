from advent03a import (
    most_common_values,
    load_file,
    convert_bin_string_to_decimal,
    reverse_most_common_values,
    multiply_numbers,
)


def keep_values_with_most_common_number(list, position):
    values = most_common_values(list)  # most common values on certain positions
    new_list = []
    for str in list:
        if str[position] == values[position]:
            new_list.append(str)
    return new_list


def rating_binary(list, func):
    for i in range(len(list)):
        if i == 0:
            new_list = func(list, 0)
        else:
            new_list = func(new_list, i)
        if len(new_list) == 1:
            return new_list
    return new_list


def keep_values_with_least_common_number(list, position):
    values = reverse_most_common_values(most_common_values(list))
    new_list = []
    for str in list:
        if str[position] == values[position]:
            new_list.append(str)
    return new_list


binary_list = load_file("binary_a.txt")
oxygen_rating = convert_bin_string_to_decimal(
    rating_binary(binary_list, keep_values_with_most_common_number)
)
co2_rating = convert_bin_string_to_decimal(
    rating_binary(binary_list, keep_values_with_least_common_number)
)
print(multiply_numbers([oxygen_rating, co2_rating]))
