# def matrix(n=1, *m, value=0):
#     if m:
#         cols = *m
#         arr = [[value] * cols for _ in range(n)]
#     else:
#         arr = [[value] * n for _ in range(n)]
#     return arr
#
# print(matrix(3, 4, 9))

#                    Функции как объекты
#      Задача 1
# numbers = [(10, 10, 10), (30, 45, 56), (81, 39), (1, 2, 3), (12,), (-2, -4, 100), (1, 2, 99), (89, 9, 34), (10, 20, 30, -2), (50, 40, 50), (34, 78, 65), (-5, 90, -1, -5), (1, 2, 3, 4, 5, 6), (-9, 8, 4), (90, 1, -45, -21)]
# def comparator(tpl):
#     return sum(tpl) / len(tpl)
# print(min(numbers, key=comparator))
# print(max(numbers, key=comparator))

    # Задача 2
# from math import sqrt
#
# points = [(-1, 1), (5, 6), (12, 0), (4, 3), (0, 1), (-3, 2), (0, 0), (-1, 3), (2, 0), (3, 0), (-9, 1), (3, 6), (8, 8)]
#
# def distance_to_0(point):
#     return sqrt(point[0] ** 2 + point[1] ** 2)
#
# print(sorted(points, key=distance_to_0))
#
#    Задача 3
# numbers = [(10, 10, 10), (30, 45, 56), (81, 80, 39), (1, 2, 3), (12, 45, 67), (-2, -4, 100), (1, 2, 99), (89, 90, 34), (10, 20, 30), (50, 40, 50), (34, 78, 65), (-5, 90, -1)]
#
# def sum_minmax(tpl):
#     return min(tpl) + max(tpl)
#
# print(sorted(numbers, key=sum_minmax))

#     Сортируй как хочешь
# def compare(x):
#     return x[i-1]
#
# athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33),
#             ('Рустам', 10, 128, 30), ('Амир', 16, 170, 70), ('Рома', 16, 188, 100),
#             ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]
# i=int(input())
# athletes.sort(key=compare)
# for item in athletes:
#     print(*item)

#     Математические функции
# from math import sin
#
# def squarex(x):
#     return x** 2
# def cubex(x):
#     return x ** 3
# def sqrtx(x):
#     return x ** 0.5
# def absx(x):
#     return abs(x)
# def sinx(x):
#     return sin(x)
#
# func = {'квадрат': squarex, 'куб': cubex, 'корень': sqrtx, 'модуль': absx, 'синус': sinx}
# n = int(input())
# print(func[input()](n))

#     Интересная сортировка
# nums = input().split()
# def sums(num):
#     return sum(int(x) for x in num)
# print(*sorted(nums, key=sums))