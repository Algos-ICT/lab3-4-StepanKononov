import math
import random


def solution(x, y): # x, y - списки координат точек типа n1 = (x[0], y[0])
    a = list(zip(x, y))  # Упаковываем в массив а кортежи координать точек
    ax = sorted(a, key=lambda x: x[0])  # ax - список точек отсортированные по X
    ay = sorted(a, key=lambda x: x[1])  # ay - список точек отсортированные по Y
    p1, p2, mi = closest_pair(ax, ay)  # Рекурсивный вызов
    return mi

def closest_pair(ax, ay):
    ln_ax = len(ax)
    if ln_ax <= 3:
        return brute(ax)  # При малом количестве точек вычисляем наивным алгоритмом
    mid = ln_ax // 2  # Средняя линия деления
    Lx = ax[:mid]  # Делим на две части (правая и левая)
    Rx = ax[mid:]
    # Коодината линии деления по X
    midpoint = ax[mid][0]

    Ly = list()
    Ry = list()
    '''
    Так как линия делит по X то Lx и Rx разделенены уже сразу, однако Ly и Ry так легко делить нельзя поэтому 
    делим их вручную
    '''
    for x in ay:  # Распределяем точки в левую и правую часть
        if x[0] <= midpoint:
           Ly.append(x)
        else:
           Ry.append(x)
    # Рекурсивный вызов для левой и правой части
    (p1, q1, mi1) = closest_pair(Lx, Ly)
    (p2, q2, mi2) = closest_pair(Rx, Ry)
    # Вычисляем минимальное расстояние среди левой и правой части
    # P.S. mn - [[x0,y0][x1,y1]], p1/p2 и q1/q2 координаты ближайщих друг к другу точек с права и слева соответсвенно
    if mi1 <= mi2:
        d = mi1
        mn = (p1, q1)
    else:
        d = mi2
        mn = (p2, q2)


    # Вызываем функцию для нахождения точек возле средней линии
    (p3, q3, mi3) = closest_split_pair(ax, ay, d, mn)

    # Сравниваем "центральное" расстояние с минимальным их правой/левой части
    if d <= mi3:
        return mn[0], mn[1], d
    else:
        return p3, q3, mi3

# Вычисление минимального расстояния просто через полный перебор
def brute(ax):
    mi = dist(ax[0], ax[1])
    p1 = ax[0]
    p2 = ax[1]
    ln_ax = len(ax)
    if ln_ax == 2:
        return p1, p2, mi
    for i in range(ln_ax-1):
        for j in range(i + 1, ln_ax):
            if i != 0 and j != 1: # Это уже вычислили (см на 5 строк выше)
                d = dist(ax[i], ax[j])
                if d < mi:
                    mi = d
                    p1, p2 = ax[i], ax[j]

    return p1, p2, mi

def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Вычисляет мин рассотояние "срединных" точек (по разные строны от линии)
def closest_split_pair(p_x, p_y, delta, best_pair):
    ln_x = len(p_x)
    mx_x = p_x[ln_x // 2][0]  # Координата линии разделения
    # Создаём подмассив точек не дальше чем дельта от
    # средней точки на массиве с сортировкой по x
    s_y = [x for x in p_y if mx_x - delta <= x[0] <= mx_x + delta]
    best = delta  # Устанавливваем минимально расстояние
    ln_y = len(s_y)
    for i in range(ln_y - 1):
        for j in range(i+1, min(i + 7, ln_y)):
            p, q = s_y[i], s_y[j]
            dst = dist(p, q)
            if dst < best:
                best_pair = p, q
                best = dst
    return best_pair[0], best_pair[1], best


print(solution([0, 3,7,7,7,], [0,4,6,5,4]))