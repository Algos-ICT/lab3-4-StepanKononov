def simple_counting_sort(A):
    scope = max(A) + 1
    C = [0] * scope
    for x in A:
        C[x] += 1
    A[:] = []
    for number in range(scope):
        A += [number] * C[number]
    return A


def convert(num, base):
    if num == 0:
        return 0
    result = ''
    while num != 0:
        result += str(num % base)
        num //= base
    return int(result[:: -1])

n = 2

test = [convert(x, n) for x in range(n ** 3 - 1, -1, -1)]

test = simple_counting_sort(test)
ans = []

for num in test:
    ans.append(int(str(num), n))

print(ans)