#                      Количество слов в тексте
# Первый вариант:
# print(len(set([''.join([i for i in z if i.isalpha()]) for z in input().lower().split()])))
# Второй вариант:
# print(len(set(x.strip('.,;:-?!') for x in input().lower().split())))

#                         Числа первой строки
# print(*sorted(set([int(i) for i in input().split()]) - set([int(j) for j in input().split()])))

