

n = int(input())

N = [x for x in range(1, n + 1)]

for i in range(2, len(N)):
    N[i], N[i // 2] = N[i // 2], N[i]

print(N)
