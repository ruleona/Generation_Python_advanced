     # Задача №1
# list_with_8 = []
# for dct in users:
#     if dct['phone'][-1] == '8':
#         list_with_8.append(dct['name'])
# print(*sorted(list_with_8), sep=' ')

#      Задача №2
# Решение курильщика:
# lst = []
# for dct in users:
#     if 'email' not in dct.keys():
#         lst.append(dct['name'])
#     else:
#         if not dct['email']:
#             lst.append(dct['name'])
# print(*sorted(lst))
#
# Решение здорового человека:
# print(*sorted([k['name'] for k in users if 'email' not in k or k['email'] == '']))




# С помощью словарного метода get(), можно упростить код в задаче о повторяющихся числах.
# numbers = [9, 8, 32, 1, 10, 1, 10, 23, 1, 4, 10, 4, 2, 2, 2, 2, 1, 10, 1, 2, 2, 32, 23, 23]
#
# result = {}
# for num in numbers:
#     result[num] = result.get(num, 0) + 1

# В Python 3.9 появились операторы | и |= которые реализуют операцию конкатенации словарей.
# Приведенный ниже код:
# info1 = {'name': 'Bob',
#         'age': 25,
#         'job': 'Dev'}
# info2 = {'age': 30,
#         'city': 'New York',
#         'email': 'bob@web.com'}
# info1 |= info2
# print(info1)
# выводит (порядок элементов может отличаться):
#
# {'name': 'Bob', 'age': 30, 'job': 'Dev', 'city': 'New York', 'email': 'bob@web.com'}
#
#          Раздел 10.3, задача №2
# dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
# dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}
#
# result = {}
# for key in dict1.keys():
#     result[key] = dict1.get(key) + dict2.get(key, 0)
# for key in dict2.keys():
#     result[key] = result.setdefault(key, dict2.get(key) + dict1.get(key, 0))
# print(*sorted(result.items(), key=lambda x: x[0]))


#          Раздел 10.3 задача 4
# s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon pomegranate banana banana orange barley apricot plum grapefruit banana quince strawberry barley grapefruit banana grapes melon strawberry apricot currant currant gooseberry raspberry apricot currant orange lime quince grapefruit barley banana melon pomegranate barley banana orange barley apricot plum banana quince lime grapefruit strawberry gooseberry apple barley apricot currant orange melon pomegranate banana banana orange apricot barley plum banana grapefruit banana quince currant orange melon pomegranate barley plum banana quince barley lime grapefruit pomegranate barley'
# words = [word for word in s.split()]
# result = {}
# for word in words:
#     result[word] = result.get(word, 0) + 1
# print(sorted(result.items(), key=lambda x: (-x[1], x[0]))[0][0])

         #
         # Раздел 10.3 задача 5
# pets = [('Hatiko', 'Parker', 'Wilson', 50),
#         ('Rusty', 'Josh', 'King', 25),
#         ('Fido', 'John', 'Smith', 28),
#         ('Butch', 'Jake', 'Smirnoff', 18),
#         ('Odi', 'Emma', 'Wright', 18),
#         ('Balto', 'Josh', 'King', 25),
#         ('Barry', 'Josh', 'King', 25),
#         ('Snape', 'Hannah', 'Taylor', 40),
#         ('Horry', 'Martha', 'Robinson', 73),
#         ('Giro', 'Alex', 'Martinez', 65),
#         ('Zooma', 'Simon', 'Nevel', 32),
#         ('Lassie', 'Josh', 'King', 25),
#         ('Chase', 'Martha', 'Robinson', 73),
#         ('Ace', 'Martha', 'Williams', 38),
#         ('Rocky', 'Simon', 'Nevel', 32)]
#
# result = {}
# for dog in pets:
#     name, owner_name, owner_surname, age = dog[0], dog[1], dog[2], dog[3]
#     key = (owner_name, owner_surname, age)
#     if key in result:
#         result[key].append(name)
#     else:
#         result[key] = [name]

        # Самое редкое слово
# words = [word.strip('.,!?:;-') for word in input().lower().split()]
# result = {}
# for word in words:
#     result[word] = result.get(word, 0) + 1
# print(sorted(result.items(), key=lambda x: (x[1], x[0]))[0][0])

        # Исправление дубликатов 🌶️
# chars = [char for char in input().split()]
# result = {}
# for char in chars:
#     if char not in result.keys():
#         print(char, end=' ')
#     else:
#         print(f'{char}_{result[char]}', end=' ')
#     result[char] = result.get(char, 0) + 1

        #Словарь программиста
# n, dct = int(input()), {}
# lst1 = [input().split(': ') for _ in range(n)]
# for el in lst1:
#     dct[el[0]] = el[1]
# lst2 = [input().lower() for _ in range(int(input()))]
# for el in lst2:
#     print(dct.get(el, 'Не найдено'))

       # Анаграммы
# dct1, dct2 = {}, {}
# lst1 = [char for char in input()]
# for char in lst1:
#     dct1[char] = dct1.get(char, 0) + 1
# lst2 = [char for char in input()]
# for char in lst2:
#     dct2[char] = dct2.get(char, 0) + 1
# print('YES' if dct1 == dct2 else 'NO')
#
#        Анаграммы 2
dct1, dct2 = {}, {}
lst1 = [char for char in input().lower() if char.isalpha()]
for char in lst1:
    dct1[char] = dct1.get(char, 0) + 1
# lst2 = [char for char in input().lower() if char.isalpha()]
# for char in lst2:
#     dct2[char] = dct2.get(char, 0) + 1
# print('YES' if dct1 == dct2 else 'NO')
#
#         Словарь синонимов
# n, dct = int(input()), {}
# lst1 = [input().split() for _ in range(n)]
# for el in lst1:
#     dct[el[0]] = el[1]
#     dct[el[1]] = el[0]
# print(dct.get(input()))

#          Страны и города
# Решение курильщика.
# n, dct = int(input()), {}
# for _ in range(n):
#     lst = input().split()
#     for i in range(1, len(lst)):
#         dct[lst[i]] = lst[0]
# lst2 = [input() for _ in range(int(input()))]
# for el in lst2:
#     print(dct.get(el))

# Решение здорового человека:
# dct = {}
# for _ in range(int(input())):
#     a, *b = input().split()
#     dct.update(dict.fromkeys(b, a))
# for _ in range(int(input())):
#     print(dct[input()])

          Телефонная книга
dct = {}
for _ in range(int(input())):
    a, b = input().split()
    if b in dct:
        dct[b] = dct[b] + ' ' + a
    else:
        dct[b] = a
for _ in range(int(input())):
    name = input()
    print((dct.get(name)) if name in dct else 'абонент не найден')
