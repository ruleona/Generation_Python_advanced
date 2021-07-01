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

