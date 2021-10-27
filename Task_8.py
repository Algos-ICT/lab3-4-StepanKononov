import math

lenght, count = map(int, input().split())

ans = []
ar_sort = False

def calculate_distance(x, y):
    return math.sqrt(x**2 + y**2)

for i in range(lenght):
    X, Y = map(int, input().split())
    if len(ans) < count:
        ans.append([X, Y])
    else:
        if not ar_sort:
            ans = sorted(ans, key=lambda ar:  calculate_distance(ar[0], ar[1]))
            ar_sort = True
        if calculate_distance(X, Y) < calculate_distance(ans[-1][0], ans[-1][1]):
            ans[-1] = [X, Y]
            min_index = -2
            while min_index >= -len(ans) and calculate_distance(X, Y) < calculate_distance(ans[min_index][0], ans[min_index][1]):
                ans[min_index],  ans[min_index + 1] = ans[min_index + 1],  ans[min_index]
                min_index -= 1
print(*ans)










