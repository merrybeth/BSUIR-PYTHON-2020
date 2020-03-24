from __future__ import print_function
import sys
import argparse


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-task')
    parser.add_argument('-path')
    parser.add_argument('-input')
    parser.add_argument('-help', action='store_true')
    return parser


def count_words():
    m_dict = {}
    if namespace.input == "1":
        with open(namespace.path) as file:
            m_list = [i.lower() for i in file.read().split()]
    elif namespace.input == "2":
        m_list = [i.lower() for i in input("введите данные ").split()]
    else:
        return 0
    for key in set(m_list):
        m_dict[key] = str(m_list.count(key))
    for key, value in m_dict.items():
        print('слов "{}"  в тексте - {} '.format(key, value))


def top_words():
    m_dict = {}
    if namespace.input == "1":
        with open(namespace.path) as file:
            m_list = [i.lower() for i in file.read().split()]
    elif namespace.input == "2":
        m_list = [i.lower() for i in input("введите данные ").split()]
    else:
        return 0

    for key in set(m_list):
        m_dict[key] = str(m_list.count(key))
    list_d = list(m_dict.items())
    list_d.sort(key=lambda i: i[1], reverse=True)
    i = 0

    for key in list_d[:10]:
        print(key[0], end=' ')
    print(sep='/n')


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1

        j -= 1
        while nums[j] > pivot:
            j -= 1

        if i >= j:
            return j

        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


def quick():
    if namespace.input == "1":
        with open(namespace.path) as file:
            for line in file:
                nums = [int(i) for i in line.split()]
    elif namespace.input == "2":
        nums = [int(i) for i in input("введите данные ").split()]
    else:
        return 0

    quick_sort(nums)
    for i in range(len(nums)):
        print(nums[i], end=' ')
    print(sep='/n')


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
            else:
                alist[k] = righthalf[j]
                j = j + 1
            k = k + 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1


def merge():
    i = 0
    if namespace.input == "1":
        with open(namespace.path) as file:
            for line in file:
                alist = [int(i) for i in line.split()]
    elif namespace.input == "2":
        alist = [int(i) for i in input("введите данные ").split()]
    else:
        return 0
    mergeSort(alist)
    for i in range(len(alist)):
        print(alist[i], end=' ')
    print(sep='/n')


def fib():
    if namespace.input == "1":
        with open(namespace.path) as file:
            n = int(file.read())
    elif namespace.input == "2":
        n = int(input("введите данные "))
    else:
        return 0

    for fib in fibonacci(n):
        print(fib, end=' ')
    print()


def fibonacci(n):
    fib1, fib2 = 0, 1
    for i in range(n):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1


if __name__ == '__main__':
    parser = createParser()
    namespace = parser.parse_args(sys.argv[1:])
    if namespace.help:
        print('-task',
              '1. count',
              '2. top',
              '3. quick sort',
              '4. merge sort',
              '5. fib',
              '-input',
              '1. from disk',
              '2. from print',
              '-path',
              'path of a file on disk', sep='\n')
    elif namespace.task == '1':
        count_words()
    elif namespace.task == '2':
        top_words()
    elif namespace.task == '3':
        quick()
    elif namespace.task == '4':
        merge()
    elif namespace.task == '5':
        fib()
    else:
        print("mistake")