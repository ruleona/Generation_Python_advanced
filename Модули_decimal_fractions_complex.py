# from decimal import *
# s = '9.73 8.84 8.92 9.60 9.32 8.97 8.53 1.26 6.62 9.85 1.85 1.80 0.83 6.75 9.74 9.11 9.14 5.03 5.03 1.34 3.52 8.09 7.89 8.24 8.23 5.22 0.30 2.59 1.25 6.24 2.14 7.54 5.72 2.75 2.32 2.69 9.32 8.11 4.53 0.80 0.08 9.36 5.22 4.08 3.86 5.56 1.43 8.36 6.29 5.13'
# nums = sorted([Decimal(i) for i in s.split()], reverse=True)
# print(sum(nums))
# print(*(nums)[:5])
#
#
#         Юный математик
# from fractions import Fraction
#
# n = int(input())
# lst1 = []
# for i in range(1, n):
#     num = Fraction(i, n - i)
#     if num < 1 and num.numerator + num.denominator == n:
#         lst1.append(num)
# max = 0
# for el in lst1:
#     if el > max:
#         max = el
# print(max)
#
#       Упорядоченные дроби
# from fractions import Fraction
# from math import gcd
#
# n = int(input())
# nums = set()
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         num = Fraction(i, j)
#         if num < 1 and gcd(i, j):
#             nums.add(num)
# print(*sorted(nums), sep='\n')

