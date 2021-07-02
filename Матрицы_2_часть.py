# #                 Таблица умножения
# n, m = int(input()), int(input())
# matrix = [[0 for j in range(m)] for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         matrix[i][j] = i * j
#         print(str(matrix[i][j]).ljust(3), end=' ')
#     print()

#                    Максимум в таблице
# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# max = -10
# for i in range(n):
#     for j in range(m):
#         if matrix[i][j] > max:
#             max = matrix[i][j]
# flag = True
# for i in range(n):
#     if flag:
#         for j in range(m):
#             if matrix[i][j] == max:
#                 print(i, j)
#                 flag = False
#                 break

#                   Обмен столбцов
# n, m = int(input()), int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# cols = list(map(int, input().split()))
# i, j = cols[0], cols[1]
# res = []
# for r in range(n):
#     for c in range(m):
#         if c == i:
#             matrix[r][i], matrix[r][j] = matrix[r][j], matrix[r][i]
# for r in range(n):
#     for c in range(m):
#         print(matrix[r][c], end=' ')
#     print()

#                   Симметричность матрицы(первый вариант)
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# flag = True
# for i in range(n):
#     if flag:
#         for j in range(len(matrix[i])):
#             if i > j and matrix[i][j] != matrix[j][i]:
#                 flag = False
#                 break
# print('YES' if flag else 'NO')

#                  Симметричность матрицы(второй вариант с all)
# n = int(input())
# matrix = [[int(j) for j in input().split()] for _ in range(n)]
# print('YES' if all([matrix[i][j] == matrix[j][i] for j in range(n) for i in range(n)]) else 'NO')

#                  Обмен диагоналей
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for i in range(n):
#     for j in range(n):
#         if j == i:
#             matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
# for i in range(n):
#     print(*matrix[i])

#                  Зеркальное отображение
# n = int(input())
# matrix = [[int(i) for i in input().split()] for _ in range(n)]
# for i in range(int(n / 2)):
#     matrix[i], matrix[n - i - 1] = matrix[n - i - 1], matrix[i]
# for i in range(n):
#     print(*matrix[i])