# #Чтобы перебрать элементы матрицы, необходимо использовать вложенные циклы.
# #Например, выведем на экран все элементы матрицы, перебирая их по строкам:

# rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
#
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
#
# for r in range(rows):
#     for c in range(cols):
#         print(matrix[r][c], end=' ')
#     print()

# #Для перебора элементов матрицы по столбцам можно использовать следующий код:
#
# rows, cols = 3, 4           # rows - количество строк, cols - количество столбцов
#
# matrix  = [[2, 3, 1, 0],
#            [9, 4, 6, 8],
#            [4, 7, 2, 7]]
#
# for c in range(cols):
#     for r in range(rows):
#         print(matrix[r][c], end=' ')
#     print()

# # Элементы с равными индексами i == j находятся на главной диагонали. Такие элементы обозначаются matrix[i][i].
# # Элементы с индексами i и j, связанными соотношением i + j + 1 = n (или j = n - i - 1),
# # где n — размерность матрицы, находятся на побочной диагонали.
# # Таким образом, чтобы установить элементы главной или побочной диагонали, достаточно одного цикла
# n = 8
# matrix = [[0]*n for _ in range(n)]    # создаем квадратную матрицу размером 8×8
#
# for i in range(n):                     # заполняем главную диагональ 1-цами, а побочную 2-ками
#     matrix[i][i] = 1
#     matrix[i][n-i-1] = 2
#
# for r in range(n):                     # выводим матрицу
#     for c in range(m):
#         print(matrix[r][c], end=' ')
#     print()

# #Используйте функцию print_matrix() для вывода квадратной матрицы размерности n:
#
# def print_matrix(matrix, n, width=1):
#     for r in range(n):
#         for c in range(n):
#             print(str(matrix[r][c]).ljust(width), end=' ')
#         print()
# #Для считывания квадратной матрицы размерности n, заполненной числами, удобно использовать следующий код:
#
# n = int(input())
# matrix = []
# for i in range(n):
#     temp = [int(num) for num in input().split()]
#     matrix.append(temp)


# #       Создание матрицы с печатью по рядам и по столбцам
# rows, columns = int(input()), int(input())
# arr = [[input() for _ in range(columns)] for _ in range(rows)]
# for row in arr:
#     print(*row)
# print()
# for i in range(columns):
#     for j in range(rows):
#         print(arr[j][i], end=' ')
#     print()

#         Считывание матрицы рядами и сумма главной диагонали
# n = int(input())
# matrix = [input().split() for _ in range(n)]
# sum = 0
# for i in range(n):
#     sum += int(matrix[i][i])
# print(sum)

# #         Максимальный в области 2 🌶️
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# max = -100    # взято число -100, так как в тестах есть отрицательные числа
# for i in range(n):
#     for j in range(n):
#         if (i >= j and i <= n - 1 - j) or (i <= j and i >= n - 1 - j):
#             if matrix[i][j] > max:
#                 max = matrix[i][j]
# print(max)

# #           Суммы четвертей (решение курильщика)
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# count_1, count_2, count_3, count_4 = 0, 0, 0, 0
# for i in range(n):
#     for j in range(n):
#         if i < j:
#             if i < n - 1 - j:
#                 count_1 += matrix[i][j]
#             elif i > n - 1 - j:
#                 count_2 += matrix[i][j]
#         elif i > j:
#             if i > n - 1 - j:
#                 count_3 += matrix[i][j]
#             elif i < n - 1 - j:
#                 count_4 += matrix[i][j]
# print(f'Верхняя четверть: {count_1}')
# print(f'Правая четверть: {count_2}')
# print(f'Нижняя четверть: {count_3}')
# print(f'Левая четверть: {count_4}')

# #              Суммы четвертей (решение здорового человека)
# n = int(input())
# matrix = [[int(num) for num in input().split()] for i in range(n)]
# print(f"Верхняя четверть: {sum(matrix[i][j] for i in range(n) for j in range(n) if i < j and i < n - 1 - j)}")
# print(f"Правая четверть: {sum(matrix[i][j] for i in range(n) for j in range(n) if j > i > n - 1 - j)}")
# print(f"Нижняя четверть: {sum(matrix[i][j] for i in range(n) for j in range(n) if i > j and i > n - 1 - j)}")
# print(f"Левая четверть: {sum(matrix[i][j] for i in range(n) for j in range(n) if j < i < n - 1 - j)}")
