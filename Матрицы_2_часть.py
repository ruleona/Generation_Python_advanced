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

