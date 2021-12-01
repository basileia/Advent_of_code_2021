from advent01a import load_file


def how_many_larger_than_previous(numbers_list):
    count = 0
    for i in range(len(numbers_list)-2):
        if i == 0:
            continue
        if sum(numbers_list[i:i+3]) > sum(numbers_list[i-1:i+2]):
            count += 1
    return count


numbers = load_file("sonar_sweep_b.txt")
print(how_many_larger_than_previous(numbers))
