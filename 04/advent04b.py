import numpy
from advent04a import load_numbers, load_boards


def winning_boards_in_order(boards):
    masked_arrays = boards
    win_boards = []
    used_numbers = []

    for num in winning_numbers:
        for i in range(len(boards)):

            if i not in used_numbers:

                masked_arrays[i] = numpy.where(masked_arrays[i] != num, masked_arrays[i], 1.5)

                for j in range(masked_arrays[i].shape[0]):

                    if numpy.all(masked_arrays[i][j] == 1.5):
                        win_boards.append(masked_arrays[i])
                        used_numbers.append(i)
                        break

                    elif True in numpy.all(masked_arrays[i] == masked_arrays[i][0, :], axis=0):
                        win_boards.append(masked_arrays[i])
                        used_numbers.append(i)
                        break
        if len(win_boards) == len(masked_arrays):
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
winning_boards, last_win_number = winning_boards_in_order(boards)
sums_ummarked_numbers = sum_of_unmarked_numbers(winning_boards[-1])
result = last_win_number * sum(sums_ummarked_numbers)
print(result)
