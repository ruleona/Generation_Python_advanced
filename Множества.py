#                      Количество слов в тексте
# Первый вариант:
# print(len(set([''.join([i for i in z if i.isalpha()]) for z in input().lower().split()])))
# Второй вариант:
# print(len(set(x.strip('.,;:-?!') for x in input().lower().split())))

#                         Числа первой строки
# print(*sorted(set([int(i) for i in input().split()]) - set([int(j) for j in input().split()])))

#                         Одинаковые цифры
# print('NO' if set(input()).isdisjoint(set(input())) else 'YES')

#                           Все цифры
# print('YES' if set(input()).issuperset(set(input())) else 'NO')

#                            Урок информатики
# Решение курильщика:
# set1, set2, set3 = set([int(i) for i in input().split()]), set([int(i) for i in input().split()]), set([int(i) for i in input().split()])
# print(*sorted((set1 & set2) - set3, reverse=True))
#
# Решение здорового человека:
# s1, s2, s3 = [set(map(int, input().split())) for _ in range(3)]
# print(*sorted((s1 & s2) - s3, reverse=True))

#                         Урок математики
# s1, s2, s3 = [set(map(int, input().split())) for _ in range(3)]
# print(*sorted((s1 | s2 | s3) - (s1 & s2 & s3)))

#                           Урок физики
# s1, s2, s3 = [set(map(int, input().split())) for _ in range(3)]
# print(*sorted(s3 - s2 - s1, reverse=True

#                            Урок биологии
# s1, s2, s3 = [set(map(int, input().split())) for _ in range(3)]
# print(*sorted({10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0} - s3 - s2 - s1))