 #          Домашнее задание
# n, m, k, p = int(input()), int(input()), int(input()), int(input())
# print(n - p - (m - p) - (k - p))

#             Восход
# values = [i for i in input().split()]
# print(len(values) - len(set(values)))

#            Города
# n = int(input())
# my_set = {input() for _ in range(n)}
# print('REPEAT' if input() in my_set else 'OK')

#           Книги на прочтение
# m, n = int(input()), int(input())
# library, lst = set(), []
# for _ in range(m):
#     library.add(input())
# for _ in range(n):
#     lst.append(input())
# for book in lst:
#     print('YES' if book in library else 'NO')

#          Странное увлечение
# numbers = sorted({int(i) for i in input().split()} & {int(j) for j in input().split()}, reverse=True)
# if numbers:
#     print(*numbers)
# else:
#     print('BAD DAY')

#          Онлайн-школа BEEGEEK 1
# set1, set2 = {int(i) for i in input().split()}, {int(i) for i in input().split()}
# print('YES' if set1 == set2 else 'NO')

#          Онлайн-школа BEEGEEK 2
# m, n = int(input()), int(input())
# set1, set2 = {input() for _ in range(m)}, {input() for _ in range(n)}
# print(len(set1.difference(set2)))

#          Онлайн-школа BEEGEEK 3
# m, n = int(input()), int(input())
# set1, set2 = {input() for _ in range(m)}, {input() for _ in range(n)}
# res = len(set1.difference(set2)) + len(set2.difference(set1))
# print(res if res else 'NO')

#          Онлайн-школа BEEGEEK 4 🌶️
# set1, set2 = {i for i in input().split()}, {i for i in input().split()}
# print(*sorted(set1.union(set2)))

#          Онлайн-школа BEEGEEK 5 🌶️
# m, n = int(input()), int(input())
# set1, set2 = {input() for _ in range(m)}, {input() for _ in range(n)}
# if len(set1) == m:
#     res = len(set1.symmetric_difference(set2))
# else:
#     res = len(set1.symmetric_difference(set2)) - abs(len(set1) - m)
# print(res if res else 'NO')

#          Онлайн-школа BEEGEEK 6 🌶️
# Решение курильщика:
# m = int(input())
# my_set = set()
# for i in range(m):
#     n = int(input())
#     new_set = {input() for _ in range(n)}
#     if i == 0:
#         my_set.update(new_set)
#     else:
#         my_set.intersection_update(new_set)
# print(*sorted(my_set), sep='\n')

# Решение здорового человека:
# s = [set(input() for _ in range(int(input()))) for _ in range(int(input()))]
# print(*sorted(set.intersection(*s)), sep='\n')

