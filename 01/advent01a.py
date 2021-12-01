def load_file(file):
    with open(file, encoding="utf-8") as file:
        all_lines = [int(line.strip()) for line in file.readlines()]
    return all_lines


def how_many_larger_than_previous_measurement(numbers_list):
    count = 0
    for i in range(len(numbers_list)):
        if i == 0:
            continue
        if numbers_list[i] > numbers_list[i-1]:
            count += 1
    return count
