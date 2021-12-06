from advent05a import load_file, reshape


def used_coordinates_count(coordinates_pairs):
    count = {}
    for pairs in coordinates_pairs:
        if (pairs[0][0] == pairs[1][0]) or (pairs[0][1] == pairs[1][1]):
            if pairs[0][1] == pairs[1][1]:
                if pairs[0][0] > pairs[1][0]:
                    for i in range(pairs[1][0], pairs[0][0] + 1):
                        if str([i, pairs[0][1]]) in count:
                            count[str([i, pairs[0][1]])] += 1
                        else:
                            count[str([i, pairs[0][1]])] = 1
                else:
                    for i in range(pairs[0][0], pairs[1][0] + 1):
                        if str([i, pairs[0][1]]) in count:
                            count[str([i, pairs[0][1]])] += 1
                        else:
                            count[str([i, pairs[0][1]])] = 1
            if pairs[0][0] == pairs[1][0]:
                if pairs[0][1] > pairs[1][1]:
                    for i in range(pairs[1][1], pairs[0][1] + 1):
                        if str([pairs[0][0], i]) in count:
                            count[str([pairs[0][0], i])] += 1
                        else:
                            count[str([pairs[0][0], i])] = 1
                else:
                    for i in range(pairs[0][1], pairs[1][1] + 1):
                        if str([pairs[0][0], i]) in count:
                            count[str([pairs[0][0], i])] += 1
                        else:
                            count[str([pairs[0][0], i])] = 1

        else:
            if pairs[0][0] > pairs[1][0]:
                if str([pairs[1][0], pairs[1][1]]) in count:
                    count[str([pairs[1][0], pairs[1][1]])] += 1
                else:
                    count[str([pairs[1][0], pairs[1][1]])] = 1
                if pairs[0][1] > pairs[1][1]:
                    for i in range(pairs[1][0] + 1, pairs[0][0] + 1):
                        pairs[1][1] += 1
                        if str([i, pairs[1][1]]) in count:
                            count[str([i, pairs[1][1]])] += 1
                        else:
                            count[str([i, pairs[1][1]])] = 1
                if pairs[0][1] < pairs[1][1]:
                    for i in range(pairs[1][0] + 1, pairs[0][0] + 1):
                        pairs[1][1] -= 1
                        if str([i, pairs[1][1]]) in count:
                            count[str([i, pairs[1][1]])] += 1
                        else:
                            count[str([i, pairs[1][1]])] = 1
            if pairs[0][0] < pairs[1][0]:
                if str([pairs[0][0], pairs[0][1]]) in count:
                    count[str([pairs[0][0], pairs[0][1]])] += 1
                else:
                    count[str([pairs[0][0], pairs[0][1]])] = 1
                if pairs[0][1] > pairs[1][1]:
                    for i in range(pairs[0][0] + 1, pairs[1][0] + 1):
                        pairs[0][1] -= 1
                        if str([i, pairs[0][1]]) in count:
                            count[str([i, pairs[0][1]])] += 1
                        else:
                            count[str([i, pairs[0][1]])] = 1
                else:
                    for i in range(pairs[0][0] + 1, pairs[1][0] + 1):
                        pairs[0][1] += 1
                        if str([i, pairs[0][1]]) in count:
                            count[str([i, pairs[0][1]])] += 1
                        else:
                            count[str([i, pairs[0][1]])] = 1
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

used_coordinates_count = used_coordinates_count(coordinates_pairs)
result = 0
for c in used_coordinates_count.values():
    if c > 1:
        result += 1
print(result)
