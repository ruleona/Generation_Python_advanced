# #Распечатать вложенный список
#
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for i in range(len(my_list)):
#     for j in range(len(my_list[i])):
#         print(my_list[i][j], end=' ')   # используем необязательный параметр end
#     print()
#
# #или
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#
# for row in my_list:
#     for elem in row:
#         print(elem, end=' ')
#     print()

# my_list = [[12, 221, 3], [41, 5, 633], [71, 8, 99]]
#
# maximum = my_list[0][0]
# minimum = my_list[0][0]
#
# for row in my_list:
#     maximum = max(row)
#     minimum = min(row)
#
# print(maximum + minimum)

# #              Треугольник Паскаля
# def pascal(n):
#     list1 = []
#     for i in range(n + 1):
#         temp_list = []
#         for j in range(i + 1):
#             if j == 0 or j == i:
#                 temp_list.append(1)
#             else:
#                 temp_list.append(list1[i-1][j] + list1[i-1][j-1])
#         list1.append(temp_list)
#         print(temp_list)
#     return list1[n]
#
# row = int(input())
# print(pascal(row))

# #                 Chunked
# def chunked(lst, n):
#     new = []
#     for i in range(len(lst)):
#         if i % n == 0:
#             new.append([lst[i]])
#         else:
#             new[-1].append(lst[i])
#     return new
#
# list_for_chunk = input().split()
# print(chunked(list_for_chunk, int(input())))

#                   Упаковка дубликатов
# list1 = input().split()
# result = []
# for i in range(len(list1)):
#     if i == 0:
#         result.append([list1[0]])
#     else:
#         if list1[i] == list1[i - 1]:
#             result[-1].append(list1[i])
#         else:
#             result.append([list1[i]])
# print(result)