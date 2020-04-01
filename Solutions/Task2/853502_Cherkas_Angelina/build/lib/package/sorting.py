import tempfile
from random import randint
import os
import random

file = "numbers.txt"
with open(file, 'w') as f:
    f.writelines('{}\n'.format(random.randint(-1000000, 1000000)) for _ in range(100000))

all_files = []


def merge_sort(sort_list):
    if len(sort_list) > 1:
        mid = len(sort_list) // 2
        left_half = sort_list[:mid]
        right_half = sort_list[mid:]

        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                sort_list[k] = left_half[i]
                i = i + 1
            else:
                sort_list[k] = right_half[j]
                j = j + 1
            k = k + 1

        while i < len(left_half):
            sort_list[k] = left_half[i]
            i = i + 1
            k = k + 1

        while j < len(right_half):
            sort_list[k] = right_half[j]
            j = j + 1
            k = k + 1


def split_files(file_path, size):
    with open(file_path, 'r') as file:
        i = 1
        temp = []
        for line in file:
            temp.append(int(line))
            i += 1
            if i > size:
                i = 1
                merge_sort(temp)
                with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
                    temp_file.writelines(f'{i}\n' for i in temp)
                    all_files.append(temp_file.name)
                temp = []


def merge_sorted_files():
    while len(all_files) > 1:
        with tempfile.NamedTemporaryFile(delete=False, mode='w') as temp_file:
            with open(all_files[0], 'r') as first, open(all_files[1], 'r') as second:
                line_of_first = first.readline()
                line_of_second = second.readline()
                while line_of_first and line_of_second:
                    if int(line_of_first) <= int(line_of_second):
                        temp_file.writelines(line_of_first)
                        line_of_first = first.readline()
                    else:
                        temp_file.writelines(line_of_second)
                        line_of_second = second.readline()

                while line_of_second:
                    temp_file.writelines(line_of_second)
                    line_of_second = second.readline()
                while line_of_first:
                    temp_file.writelines(line_of_first)
                    line_of_first = first.readline()
                all_files.append(temp_file.name)

        if os.path.exists(first.name):
            all_files.pop(0)
            os.remove(first.name)

        if os.path.exists(second.name):
            all_files.pop(0)
            os.remove(second.name)


if __name__ == '__main__':
    split_files(file, 5)
    merge_sorted_files()
    with open(all_files[0], 'r') as file:
        with open("sorted_numbers.txt", 'w') as sorted:
            for line in file:
                sorted.writelines(line)


