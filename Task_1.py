"""Реализация quick_sort"""

from random import randint
from time import perf_counter
from prettytable import PrettyTable

original_array = [randint(-10**4, 10**4) for x in range(10**5)]
array_version_1 = original_array[:]
array_version_2 = original_array[:]
array_version_3 = original_array[:]
array_version_4 = original_array[:]
array_len = len(original_array)

print("Progress: 0%")
t_start = perf_counter()
def quick_sort(A, left, right):
    if left < right:
        x = A[left]
        j = left
        for i in range(left + 1, right):
            if A[i] <= x:
                j += 1
                A[j], A[i] = A[i], A[j]
        A[left], A[j] = A[j], A[left]
        quick_sort(A, left, j)
        quick_sort(A, j + 1, right)
quick_sort(array_version_1, 0, array_len)
time_1 = perf_counter() - t_start

print("Progress: 25%")
t_start = perf_counter()
def randomize_quick_sort(A, left, right):
    if left < right:
        k = randint(left, right-1)
        A[left], A[k] = A[left], A[k]
        x = A[left]
        j = left
        for i in range(left + 1, right):
            if A[i] <= x:
                j += 1
                A[j], A[i] = A[i], A[j]
        A[left], A[j] = A[j], A[left]
        randomize_quick_sort(A, left, j)
        randomize_quick_sort(A, j + 1, right)
randomize_quick_sort(array_version_2, 0, array_len)
time_2 = perf_counter() - t_start

print("Progress: 50%")
t_start = perf_counter()
def quick_sort_equals(A, left, right):
    if left < right:
        x = A[left]
        m1 = left
        m2 = m1
        for i in range(left + 1, right):
            if A[i] < x:
                m1 += 1
                m2 += 1
                A[m2], A[i] = A[i], A[m2]
                A[m1], A[m2] = A[m2], A[m1]
            elif A[i] == x:
                m2 += 1
                A[m2], A[i] = A[i], A[m2]
        A[left], A[m1] = A[m1], A[left]
        quick_sort_equals(A, left, m1)
        quick_sort_equals(A, m2 +1, right)
quick_sort_equals(array_version_3, 0, array_len)
time_3 = perf_counter() - t_start

print("Progress: 75%")
t_start = perf_counter()
def quick_sort_equals_random(A, left, right):
    if left < right:
        k = randint(left, right-1)
        A[left], A[k] = A[left], A[k]
        x = A[left]
        m1 = left
        m2 = m1
        for i in range(left + 1, right):
            if A[i] < x:
                m1 += 1
                m2 += 1
                A[m2], A[i] = A[i], A[m2]
                A[m1], A[m2] = A[m2], A[m1]
            elif A[i] == x:
                m2 += 1
                A[m2], A[i] = A[i], A[m2]
        A[left], A[m1] = A[m1], A[left]
        quick_sort_equals_random(A, left, m1)
        quick_sort_equals_random(A, m2 +1, right)
quick_sort_equals_random(array_version_4, 0, array_len)
time_4 = perf_counter() - t_start

print("Progress: 100%")
columns = ["Тип сортировки", "Время работы"]
sort_name = ["Обычная сортировка", "Рандомная сортировка", "Равная сортировка", "Рандомная равная сортировка"]
sort_time = [time_1, time_2, time_3, time_4]

ans_table = PrettyTable()
ans_table.add_column(columns[0], sort_name)
ans_table.add_column(columns[1], sort_time)
print(ans_table)

'''
print("Время работы обычной сортировки: %s секунд " % time_1)
print("Время работы рандомной сортировки: %s секунд " % time_2)
print("Время работы сортировки с учетом равных элементов: %s секунд " % time_3)
print("Время работы рандомной сортировки с учетом равных элементов: %s секунд " % time_4)
'''