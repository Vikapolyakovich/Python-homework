# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а
# Катя – школьница. Петя помогает Кате по математике. Он задумывает
# два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S
# и их произведение P. Помогите Кате отгадать задуманные Петей числа.

import math

x = int(input("Сумма двух чисел: "))
if x > 1000:
    int(input("Введите число <= 1000"))
y = int(input("Произведение двух чисел: "))
if y > 1000:
    int(input("Введите число <= 1000"))

D = (x*x) - (4 * (-1) * (-y))
d = math.sqrt(D)
k1 = (-x + d) / 2 * (-1)
k2 = x - k1
print(k1, k2)
