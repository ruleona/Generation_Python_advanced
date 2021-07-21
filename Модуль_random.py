#              Игра в Бинго
# Решение курильщика:
#
# import random
#
# matrix = [[0]*5 for _ in range(5)]
# numbers = random.sample([i for i in range(1, 75)], 25)
# count = 0
# for r in range(5):
#     for c in range(5):
#         matrix[r][c] = numbers[count]
#         count += 1
# matrix[2][2] = 0
# for r in range(5):
#     for c in range(5):
#         print(str(matrix[r][c]).ljust(3), end=' ')
#     print()

# Решение здорового человека:
# from random import sample
#
# nums = iter(sample(list(range(1, 76)), 24))
# [print(*('0  ' if i == j == 2 else str(next(nums)).ljust(3) for j in range(5))) for i in range(5)]

#                    Генератор паролей 1
# Мой вариант:
# import random, string
#
# lst1 = [char for char in string.ascii_letters if char not in 'IiLlOo']
# lst2 = [char for char in string.digits if char not in '01']
# lst1.extend(lst2)
#
#
# def generate_password(length):
#     res = ''
#     for _ in range(length):
#         res += random.choice(lst1)
#     return res
#
#
# def generate_passwords(count, length):
#     for _ in range(count):
#         print(generate_password(length))
#
# n, m = int(input()), int(input())
# generate_passwords(n, m)

# Вариант пользователя Владимир Шавров:
# import string, random
#
# def generate_password(length):
#     symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits[2:]
#     symbols = ''.join([symbol for symbol in symbols if symbol not in "lIoO"])
#     return ''.join(random.sample(symbols, length))
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n, m), sep='\n')

#                  Генератор паролей 2
# import string, random
#
# def generate_password(length):
#     symbols = string.ascii_uppercase + string.ascii_lowercase + string.digits[2:]
#     symbols = ''.join([symbol for symbol in symbols if symbol not in "IiLlOo"])
#     while True:
#         ans = ''.join(random.sample(symbols, length))
#         if all([len(set(ans).intersection(set(string.ascii_uppercase))), len(set(set(ans).intersection(string.ascii_lowercase))), len(set(ans).intersection(set(string.digits)))]):
#             break
#     return ans
#
# def generate_passwords(count, length):
#     return [generate_password(length) for _ in range(count)]
#
# n, m = int(input()), int(input())
# print(*generate_passwords(n, m), sep='\n')

