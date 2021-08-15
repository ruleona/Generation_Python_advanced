#              Входная строка
# with open('output.txt', 'w', encoding='utf-8') as file:
#     file.write(input())




#              Случайные числа
# from random import randint
#
# with open('random.txt', 'w', encoding='utf-8') as output:
#     for _ in range(25):
#         print(str(randint(111, 777)), file=output)




#              Нумерация строк
# with open('input.txt', 'r') as input, open('output.txt', 'w') as output:
#     content = input.readlines()
#     for n, string in enumerate(content):
#         output.write(f'{n + 1}) {string}')





#             Подарок на Новый Год
# with open('class_scores.txt', 'r', encoding='utf-8') as input, open('new_scores.txt', 'w', encoding='utf-8') as output:
#     content = [(el.strip() for el in line.split()) for line in input.readlines()]
#     for (name, score) in content:
#         if int(score) > 95:
#             output.write(f'{name} 100\n')
#         else:
#             output.write(f'{name} {str(int(score) + 5)}\n')




#              Загадка от Жака Фреско
# with open('goats.txt', 'r', encoding='utf-8') as input, open('answer.txt', 'w', encoding='utf-8') as output:
#     content = [line.replace('\n', '') for line in input.readlines()]
#     content.remove('COLOURS')
#     colours = {}
#     for line in content:
#         if line == 'GOATS':
#             break
#         colours.setdefault(line, 0)
#     for el in content[content.index('GOATS') + 1:]:
#         colours[el] += 1
#     result = list(filter(lambda para: para[1] > 7, colours.items()))
#     for el in result:
#         output.write(el[0] + '\n')




#              Конкатенация файлов
# with open('output.txt', 'a', encoding='utf-8') as output:
#     for _ in range(int(input())):
#         with open(input(), 'r', encoding='utf-8') as file:
#             output.writelines(file.readlines())






#            Лог файл
# Решение Санжара Абдуллаева:
# from datetime import datetime
#
# with open('logfile.txt', encoding='utf-8') as logfile, open('output.txt', 'w') as output:
#     for log in logfile.read().split('\n'):
#         name, first_time, second_time = log.split(', ')
#         delta = datetime.strptime(second_time, "%H:%M") - datetime.strptime(first_time, "%H:%M")
#         if delta.seconds >= 3600:
#             print(name, file=output)


# Мое решение:
# def time_in_minutes(time):
#     hours, minutes = map(int, time.split(':'))
#     return hours * 60 + minutes
#
# with open('logfile.txt', 'r', encoding='utf-8') as file1, open('output.txt', 'w', encoding='utf-8') as file2:
#     content = [line.strip() for line in file1.readlines()]
#     for line in content:
#         name, time1, time2 = line.split(', ')
#         if time_in_minutes(time2) - time_in_minutes(time1) >= 60:
#             file2.write(f'{name}\n')



#            Суммарная стоимость
# with open('ledger.txt', 'r') as file:
#     content = [int(line.replace('$', '').strip()) for line in file.readlines()]
#     print(f'${sum(content)}')



            # Goooood students
# with open('grades.txt', 'r', encoding='utf-8') as file:
#     content = [[el.strip() for el in line.split()] for line in file.readlines()]
#     count = 0
#     for line in content:
#         if all([bool(int(el) >= 65) for el in line[1:]]):
#             count += 1
#     print(count)
#




            # Самое длиное слово в файле
# with open('words.txt', 'r', encoding='utf-8') as file:
#     content = [word for word in file.read().split()]
#     max_len = len(max(content, key=len))
#     print(*filter(lambda x: len(x) == max_len, content), sep='\n')





#           Tail of a File
# with open(input(), 'r', encoding='utf-8') as file:
#     content = [line.strip() for line in file.readlines()]
#     if len(content) <= 10:
#         print(*content, sep='\n')
#     else:
#         print(*content[-10:], sep='\n')




                # Транслитерация 🌶️
# d = { 'а': 'a', 'к': 'k', 'х': 'h', 'б': 'b', 'л': 'l', 'ц': 'c', 'в': 'v', 'м': 'm', 'ч': 'ch', 'г': 'g', 'н': 'n', 'ш': 'sh', 'д': 'd', 'о': 'o', 'щ': 'shh', 'е': 'e', 'п': 'p', 'ъ': '*', 'ё': 'jo', 'р': 'r', 'ы': 'y', 'ж': 'zh', 'с': 's', 'ь': "'", 'з': 'z', 'т': 't', 'э': 'je', 'и': 'i', 'у': 'u', 'ю': 'ju', 'й': 'j', 'ф': 'f', 'я': 'ya', 'А': 'A', 'К': 'K', 'Х': 'H', 'Б': 'B', 'Л': 'L', 'Ц': 'C', 'В': 'V', 'М': 'M', 'Ч': 'Ch', 'Г': 'G', 'Н': 'N', 'Ш': 'Sh', 'Д': 'D', 'О': 'O', 'Щ': 'Shh', 'Е': 'E', 'П': 'P', 'Ъ': '*', 'Ё': 'Jo', 'Р': 'R', 'Ы': 'Y', 'Ж': 'Zh', 'С': 'S', 'Ь': "'", 'З': 'Z', 'Т': 'T', 'Э': 'Je', 'И': 'I', 'У': 'U', 'Ю': 'Ju', 'Й': 'J', 'Ф': 'F', 'Я': 'Ya' }
#
# with open('cyrillic.txt', 'r', encoding='utf-8') as file1, open('transliteration.txt', 'w', encoding='utf-8') as file2:
#     content = file1.read()
#     for char in content:
#         if char in d:
#             file2.write(d[char])
#         else:
#             file2.write(char)



#             Пропущенные комменты 🌶️
# with open(input(), 'r') as file:
#     content = file.readlines()
#     without_name = []
#     for i in range(len(content)):
#         if content[i].startswith('def'):
#             if content[i - 1].startswith('#'):
#                 continue
#             else:
#                 without_name.append(content[i][4: content[i].index('(')])
#     if without_name:
#         print(*without_name, sep='\n')
#     else:
#         print('Best Programming Team')