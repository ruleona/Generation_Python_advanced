        # Письмо для экзамена
# def generate_letter(mail, name, date, time, place, teacher = 'Тимур Гуев', number = '17'):
#     return f'To: {mail}\nПриветствую, {name}!\nВам назначен экзамен, который пройдет {date}, в {time}.\nПо адресу: {place}.\nЭкзамен будет проводить {teacher} в кабинете {number}.\nЖелаем удачи на экзамене!'
#
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00', 'Часова 23, корпус 2'))
# print()
# print(generate_letter('lara@yandex.ru', 'Лариса', '10 декабря', '12:00',
#                       'Часова 23, корпус 2', 'Василь Ярошевич', 23))






         # Pretty print
# def pretty_print(data, side='-', delimiter='|'):
#     sum = 1
#     for el in data:
#         sum += len(str(el)) + 3
#     print(' ' + side * (sum - 2))
#     print(delimiter, end='')
#     for el in data:
#         print(' ' + str(el) + ' ' + delimiter, end='')
#     print('\n ' + side * (sum - 2))
#
# pretty_print([1, 2, 10, 23, 123, 3000])
# pretty_print(['abc', 'def', 'ghi', '12345'])
# pretty_print(['abc', 'def', 'ghi'], side='*')
# pretty_print(['abc', 'def', 'ghi'], delimiter='#')
# pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')






# def concat(*args, sep=' '):
#     return sep.join(list(map(str, args)))
#
# print(concat('hello', 'python', 'and', 'stepik'))
# print(concat('hello', 'python', 'and', 'stepik', sep='*'))
# print(concat('hello', 'python', sep='()()()'))
# print(concat('hello', sep='()'))
# print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))







# from functools import reduce
#
# def product_of_odds(data):
#     return reduce(lambda x, y: x * y, list(filter(lambda x: x % 2 == 1, data)), 1)







#          Гематрия слова
# words = [input() for _ in range(int(input()))]
# words = sorted(words)
# print(*sorted(words, key=lambda word: sum([ord(letter) - ord('A') for letter in word.upper()])), sep='\n')







         # Сортировка IP-адресов
# ips = [input().split('.') for _ in range(int(input()))]
# ips = sorted(ips, key=lambda ip: (int(ip[0]) * 256 ** 3 + int(ip[1]) * 256 ** 2 + int(ip[2]) * 256 ** 1 + int(ip[3] * 256 ** 0)))
# for ip in ips:
#     print('.'.join(ip))

# words = 'the world is mine take a look what you have started'.split()
#
# print(*list(map(lambda x: '"' + x + '"', words)))






# numbers = [18, 191, 9009, 5665, 78, 77, 45, 23, 19991, 908, 8976, 6565, 5665, 10, 1000, 908, 909, 232, 45654, 786]
# print(*filter(lambda x: str(x) != str(x)[::-1], numbers))






# numbers = [(10, -2, 3, 4), (-13, 56), (1, 9, 2), (-1, -9, -45, 32), (-1, 5, 1), (17, 0, 1), (0, 1), (3,), (39, 12), (11, -23), (10, -100, 21, 32), (3, -8), (1, 1)]
# sorted_numbers = sorted(numbers, key=lambda x: sum(x) / len(x), reverse=True)
# print(sorted_numbers)





# def call(func, *args):
#     return func(*args)





# def compose(f, g):
#     def inner_func(x):
#         return f(g(x))
#     return inner_func





# from operator import *
#
# def arithmetic_operation(operation):
#     operations = {'+': add, '-': sub, '/': truediv, '*': mul}
#     return operations[operation]






words = [input() for _ in range(int(input())]


