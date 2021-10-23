"""Реализация quick_sort"""

from random import randint
from time import perf_counter

N = [randint(-10, 10) for x in range(100000)]
copyAr = N[:]

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

quick_sort_equals(N, 0, len(N))

print(N == sorted(copyAr))

'''
A = [6,4,2,3,9,8,9,4,7,6,1,6]
left = 0
right = len(A)
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

print(A)'''