import statistics


def load_file(file):
    with open(file, encoding="utf-8") as file:
        numbers = file.read().replace("\n", "").split(",")
        return list(map(int, numbers))


# Solution 1
def fuel_consumption(place, positions):
    sum = 0
    for position in positions:
        sum += abs(position - place)
    return sum


# Solution 2
def fuel_consumption_2(place, positions):
    result = 0
    for position in positions:
        number_of_fields = int(abs(position - place))
        result += sum(range(number_of_fields + 1))
    return result


numbers = load_file("input.txt")

# Solution 1
place = statistics.median(numbers)
print(fuel_consumption(place, numbers))

# Solution 2
place2 = int(statistics.mean(numbers))
result = fuel_consumption_2(place2, numbers)
print(result)
