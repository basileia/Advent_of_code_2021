from functools import reduce
from operator import mul


def reshape(lst, shape):
    if len(shape) == 1:
        return lst
    n = reduce(mul, shape[1:])
    return [reshape(lst[i * n : (i + 1) * n], shape[1:]) for i in range(len(lst) // n)]


def load_file(file):
    coordinates = []
    with open(file, encoding="utf-8") as file:
        instructions = file.read().split("\n")

        for coord in instructions:
            coord = coord.split(" -> ")
            coordinates.append(coord)
    return coordinates


def used_coordinates_count(coordinates_pairs):
    used = []
    count = {}
    for pairs in coordinates_pairs:
        if pairs[0][1] == pairs[1][1]:
            if pairs[0][0] > pairs[1][0]:
                for i in range(pairs[1][0], pairs[0][0] + 1):
                    used.append([i, pairs[0][1]])
                    if str([i, pairs[0][1]]) in count:
                        count[str([i, pairs[0][1]])] += 1
                    else:
                        count[str([i, pairs[0][1]])] = 1
            else:
                for i in range(pairs[0][0], pairs[1][0] + 1):
                    used.append([i, pairs[0][1]])
                    if str([i, pairs[0][1]]) in count:
                        count[str([i, pairs[0][1]])] += 1
                    else:
                        count[str([i, pairs[0][1]])] = 1
        if pairs[0][0] == pairs[1][0]:
            if pairs[0][1] > pairs[1][1]:
                for i in range(pairs[1][1], pairs[0][1] + 1):
                    used.append([pairs[0][0], i])
                    if str([pairs[0][0], i]) in count:
                        count[str([pairs[0][0], i])] += 1
                    else:
                        count[str([pairs[0][0], i])] = 1
            else:
                for i in range(pairs[0][1], pairs[1][1] + 1):
                    used.append([pairs[0][0], i])
                    if str([pairs[0][0], i]) in count:
                        count[str([pairs[0][0], i])] += 1
                    else:
                        count[str([pairs[0][0], i])] = 1
    return count


coordinates = load_file("venture_a.txt")

new = []
for coord in coordinates:
    for i in range(len(coord)):
        coord[i] = coord[i].split(",")
        new.append(coord[i])

coordinates_pairs = reshape(new, [2, 2])

# string pairs tu num pairs
for i in range(len(coordinates_pairs)):
    for j in range(len(coordinates_pairs[i])):
        for k in range(len(coordinates_pairs[i][j])):
            coordinates_pairs[i][j][k] = int(coordinates_pairs[i][j][k])

for pairs in coordinates_pairs:
    if (pairs[0][0] == pairs[1][0]) or (pairs[0][1] == pairs[1][1]):
        continue
    else:
        coordinates_pairs.remove(pairs)

used_coordinates_count = used_coordinates_count(coordinates_pairs)
result = 0
for c in used_coordinates_count.values():
    if c > 1:
        result += 1
