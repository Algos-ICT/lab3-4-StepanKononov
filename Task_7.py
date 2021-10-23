
from string import ascii_lowercase

n, k, length = map(int, input().split())

A = ['bbb', 'aba', 'baa']
rang = len(ascii_lowercase)

correspondence = dict()
for i in range(len(ascii_lowercase)):
    correspondence[ascii_lowercase[i]] = i + 1

temp = dict()
for i in range(len(A)):
    temp[A[i]] = i + 1




for i in range(length):
    B = [[] for k in range(rang)] #список длины range, состоящий из пустых списков
    for x in A:
        figure = x[-(i+1)]
        B[correspondence[figure]].append(x)

    A = []
    for k in range(rang):
        A = A + B[k]

for i in A:
    print(temp[i], end=' ')
print()
print(A)