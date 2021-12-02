import numpy


def load_file(file):
    with open(file, encoding="utf-8") as file:
        all_lines = [line.strip().split() for line in file.readlines()]
    return all_lines


def deep_dive(instructions):
    position = [0, 0]
    for inst in instructions:
        if "forward" in inst:
            position[0] += int(inst[1])
        elif "down" in inst:
            position[1] += int(inst[1])
        elif "up" in inst:
            position[1] -= int(inst[1])
    return position


def multiply_position(numbers):
    return numpy.prod(numbers)
