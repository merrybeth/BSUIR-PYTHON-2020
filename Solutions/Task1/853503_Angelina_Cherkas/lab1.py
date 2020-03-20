from __future__ import print_function
import sys
import argparse
import random
from random import randint


def createParser():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', nargs='+')
    return parser


def task1():
    m_dict = {}
    with open(namespace.name[1]) as file:
        m_list = [i.lower() for i in file.read().split()]
    for key in set(m_list):
        m_dict[key] = str(m_list.count(key))
    for key, value in m_dict.items():
        print('слов "{}"  в тексте - {} '.format(key, value))


def task2():
    m_dict = {}
    with open(namespace.name[1]) as file:
        m_list = [i.lower() for i in file.read().split()]
    for key in set(m_list):
        m_dict[key] = str(m_list.count(key))
    list_d = list(m_dict.items())
    list_d.sort(key=lambda i: i[1], reverse=True)
    i = 0
    list_d = dict(list_d)
    for key in list_d[:10]:
        print(key, end=' ')
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


def task3():
    with open(namespace.name[1]) as f:
        for line in f:
            nums = [int(i) for i in line.split()]
    quick_sort(nums)
    for i in range(len(nums)):
        print(nums[i], end=' ')
    print(sep='/n')


def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist)//2
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
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i+1
            k = k+1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j+1
            k = k+1


def task4():
    i = 0
    with open(namespace.name[1]) as f:
        for line in f:
            alist = [int(i) for i in line.split()]
    mergeSort(alist)
    for i in range(len(alist)):
        print(alist[i], end=' ')
    print(sep='/n')


def task5():
    with open(namespace.name[1]) as f:
        n = int(f.read())-2
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
    if namespace.name[0] == '1':
        task1()
    elif namespace.name[0] == '2':
        task2()
    elif namespace.name[0] == '3':
        task3()
    elif namespace.name[0] == '4':
        task4()
    elif namespace.name[0] == '5':
        task5()
    else:
        print("mistake")

