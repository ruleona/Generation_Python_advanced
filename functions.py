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

#      Интересная сортировка - 2
# nums = input().split()
# nums.sort(key=lambda x: int(x))
# print(nums)
# def sums(num):
#     return sum(int(x) for x in num)
# print(*sorted(nums, key=sums))

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
#
# def roundx(num):
#     return round(num, 2)
#
# numbers = [3.56773, 5.57668, 4.00914, 56.24241, 9.01344, 32.12013, 23.22222, 90.09873, 45.45, 314.1528, 2.71828, 1.41546]
# print(*map(roundx, numbers), sep='\n')

# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
# def is_3zn(num):
#     return 99 < num < 1000 and num % 5 == 2
# def cubes(num):
#     return num ** 3
# numbers = [1014, 1321, 675, 1215, 56, 1386, 1385, 431, 1058, 486, 1434, 696, 1016, 1084, 424, 1189, 475, 95, 1434, 1462, 815, 776, 657, 1225, 912, 537, 1478, 1176, 544, 488, 668, 944, 207, 266, 1309, 1027, 257, 1374, 1289, 1155, 230, 866, 708, 144, 1434, 1163, 345, 394, 560, 338, 232, 182, 1438, 1127, 928, 1309, 98, 530, 1013, 898, 669, 105, 130, 1363, 947, 72, 1278, 166, 904, 349, 831, 1207, 1496, 370, 725, 926, 175, 959, 1282, 336, 1268, 351, 1439, 186, 273, 1008, 231, 138, 142, 433, 456, 1268, 1018, 1274, 387, 120, 340, 963, 832, 1127]
# print(*map(cubes, filter(is_3zn, numbers)), sep='\n')


# def reduce(operation, items, initial_value):
#     acc = initial_value
#     for item in items:
#         acc = operation(acc, item)
#     return acc
# def square(acc, num):
#     return acc + num ** 2
# numbers = [97, 42, 9, 32, 3, 45, 31, 77, -1, 11, -2, 75, 5, 51, 34, 28, 46, 1, -8, 84, 16, 51, 90, 56, 65, 90, 23, 35, 11, -10, 70, 90, 90, 12, 96, 58, -8, -4, 91, 76, 94, 60, 72, 43, 4, -6, -5, 51, 58, 60, 30, 38, 67, 62, 36, 72, 34, 82, 62, -1, 60, 82, 87, 81, -7, 57, 26, 36, 17, 43, 80, 40, 75, 94, 91, 64, 38, 72, 29, 84, 38, 35, 7, 54, 31, 95, 78, 27, 82, 1, 64, 94, 31, 29, -8, 98, 24, 61, 7, 73]
# print(reduce(square, numbers, 0))



# def map(function, items):
#     result = []
#     for item in items:
#         result.append(function(item))
#     return result
# def filter(function, items):
#     result = []
#     for item in items:
#         if function(item):
#             result.append(item)
#     return result
# def square(x):
#     return x ** 2
# def is_2zn(x):
#     return 9 < abs(x) < 100 and abs(x) % 7 == 0
# numbers = [77, 293, 28, 242, 213, 285, 71, 286, 144, 276, 61, 298, 280, 214, 156, 227, 228, 51, -4, 202, 58, 99, 270, 219, 94, 253, 53, 235, 9, 158, 49, 183, 166, 205, 183, 266, 180, 6, 279, 200, 208, 231, 178, 201, 260, -35, 152, 115, 79, 284, 181, 92, 286, 98, 271, 259, 258, 196, -8, 43, 2, 128, 143, 43, 297, 229, 60, 254, -9, 5, 187, 220, -8, 111, 285, 5, 263, 187, 192, -9, 268, -9, 23, 71, 135, 7, -161, 65, 135, 29, 148, 242, 33, 35, 211, 5, 161, 46, 159, 23, 169, 23, 172, 184, -7, 228, 129, 274, 73, 197, 272, 54, 278, 26, 280, 13, 171, 2, 79, -2, 183, 10, 236, 276, 4, 29, -10, 41, 269, 94, 279, 129, 39, 92, -63, 263, 219, 57, 18, 236, 291, 234, 10, 250, 0, 64, 172, 216, 30, 15, 229, 205, 123, -105]
# print(sum(map(square, filter(is_2zn, numbers))))