def load_file(file):
    with open(file, encoding="utf-8") as file:
        list = file.read().replace("\n", "").split(",")
        fish_dict = {}
        for num in list:
            fish_dict[int(num)] = list.count(num)
        return dict(sorted(fish_dict.items()))


def lanternfish(dict_fish):

    new_dict = dict(dict_fish)

    for key in dict_fish:

        if key == 0:
            if 6 in new_dict:
                new_dict[6] += dict_fish[0]
            else:
                new_dict[6] = dict_fish[0]
            if 8 in new_dict:
                new_dict[8] += dict_fish[0]
            else:
                new_dict[8] = dict_fish[0]
            new_dict[0] = 0

        else:
            if (key - 1) in new_dict:
                new_dict[key - 1] += dict_fish[key]

            else:

                new_dict[key - 1] = dict_fish[key]

            if key in new_dict:

                new_dict[key] -= dict_fish[key]

    return dict(sorted(new_dict.items()))


fish = load_file("input.txt")
dict_fish = lanternfish(fish)

# Solution 1
# for i in range(79):
#     dict_fish = lanternfish(dict_fish)

# Solution 2
for i in range(255):
    dict_fish = lanternfish(dict_fish)

print(sum(dict_fish.values()))
