from advent02a import load_file, multiply_position


def deep_dive_new(instructions):
    position = [0, 0, 0]
    for inst in instructions:
        if "forward" in inst:
            position[0] += int(inst[1])
            position[1] += (position[2] * int(inst[1]))
        elif "down" in inst:
            position[2] += int(inst[1])
        elif "up" in inst:
            position[2] -= int(inst[1])
    return position


list = load_file("dive_a.txt")

print(multiply_position(deep_dive_new(list)[0:2]))
