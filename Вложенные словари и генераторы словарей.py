# s = '1:men 2:kind 90:number 0:sun 34:book 56:mountain 87:wood 34:car 3:island 88:power 7:box 17:star 101:ice'
# result = {int(item.split(':')[0]): item.split(':')[1] for item in s.split()}
# print(result)

# numbers = [34, 10, 4, 6, 10, 23, 90, 100, 21, 35, 95, 1, 36, 38, 19, 1, 6, 87, 1000, 13456, 360]
# result = {n: [i for i in range(1, n + 1) if n % i == 0] for n in numbers}
# print(result)




                 # Экзамен на словари
# emails = {'nosu.edu': ['timyr', 'joseph', 'svetlana.gaeva', 'larisa.mamuk'],
#           'gmail.com': ['ruslan.chaika', 'rustam.mini', 'stepik-best'],
#           'msu.edu': ['apple.fruit', 'beegeek', 'beegeek.school'],
#           'yandex.ru': ['surface', 'google'],
#           'hse.edu': ['tomas-henders', 'cream.soda', 'zivert'],
#           'mail.ru': ['angel.down', 'joanne', 'the.fame.moster']}
# items = []
# for key, value in emails.items():
#     for el in value:
#         items.append(el + '@' + key)
# print(*sorted(items), sep='\n')
#
# dna_rna = {'A': 'U', 'C': 'G', 'G': 'C', 'T': 'A'}
# for char in input():
#     print(dna_rna[char], end='')

#            Порядковый номер
# counter = {}
# for el in input().split():
#     counter[el.strip()] = counter.get(el, 0) + 1
#     print(counter[el.strip()], end=' ')


# def merge(values):      # values - это список словарей
#     result = {}
#     for dct in values:
#         for key in dct.keys():
#             if key not in result:
#                 result[key] = {dct[key]}
#             else:
#                 result[key].add(dct[key])
#     return result
# print(merge([{'a': 1, 'b': 2}, {'b': 10, 'c': 100}, {'a': 1, 'b': 17, 'c': 50}, {'a': 5, 'd': 777}]))


   # Нерешенная задача, в коде присутствует ошибка. Возможно, не одна.
# buyers = {}
# for _ in range(int(input())):
#     name, item, quantity = input().split()
#     if name not in buyers:
#         buyers[name] = [dict(item, int(quantity))]
#     else:
#         buyers[name].append(dict(item, quantity))
#     if item in buyers[name]:
#         buyers[name][1] += int(quantity)
# print(buyers)
#
# for key, value in sorted(buyers.items()):
#     print(key)
#     print(*sorted(value, key=lambda para: para[0]))
