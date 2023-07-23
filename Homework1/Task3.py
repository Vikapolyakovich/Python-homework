# Задача 14: Требуется вывести все целые степени двойки
# (т.е. числа вида 2^k), не превосходящие числа N.

count = 0
result = 0
n = int(input("Введите число: "))
for x in range(n):
    result = 2 ** count
    if result <= n:
        print("2^", count, "=", result)
        count += 1
