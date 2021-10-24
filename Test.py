
import math

def calculate_distance(x, y):
    return math.sqrt(x**2 + y**2)

ans = [ [6, 6], [1, 1], [3, 3] ]


ans = sorted(ans, key=lambda ar:  math.sqrt(ar[0]**2 + ar[1]**2))



X,Y = 1, 0

if calculate_distance(X, Y) < calculate_distance(ans[-1][0], ans[-1][1]):
    ans[-1] = [X, Y]
    min_index = -2
    while min_index >= -len(ans) and calculate_distance(X, Y) < calculate_distance(ans[min_index][0], ans[min_index][1]):
        ans[min_index], ans[min_index + 1] = ans[min_index + 1], ans[min_index]
        min_index -= 1

print(ans)

