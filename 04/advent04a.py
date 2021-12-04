import numpy


def load_numbers(file):
    numbers = []
    with open(file, encoding="utf-8") as file:
        for line in file:
            for s in line.split(","):
                num = int(s)
                numbers.append(num)
    return numbers


def load_boards(file):
    a = numpy.loadtxt(file)
    num = int((len(a)*5)/25)
    a = a.reshape(num, 5, 5)
    return a


def pick_winning_boards(boards):
    masked_arrays = boards
    win_boards = []
    for num in winning_numbers:
        for i in range(len(boards)):
            masked_arrays[i] = numpy.where(masked_arrays[i] != num, masked_arrays[i], 1.5)
            for j in range(masked_arrays[i].shape[0]):
                if numpy.all(masked_arrays[i][j] == 1.5):
                    win_boards.append(masked_arrays[i])
                if True in numpy.all(masked_arrays[i] == masked_arrays[i][0, :], axis=0):
                    win_boards.append(masked_arrays[i])
        if len(win_boards) >= 1:
            return win_boards, num
    return win_boards


def sum_of_unmarked_numbers(array):
    sums = []
    for arr in array:
        new_array = numpy.where(arr != 1.5, arr, 0)
        sums.append(numpy.sum(new_array))
    return sums


winning_numbers = load_numbers("numbers_a.txt")
boards = load_boards("boards_a.txt")
winning_boards, win_number = pick_winning_boards(boards)
sums_ummarked_numbers = sum_of_unmarked_numbers(winning_boards)
result = win_number * sum(sums_ummarked_numbers)
