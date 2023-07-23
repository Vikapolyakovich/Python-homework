# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх
# решкой, а некоторые – гербом. Определите минимальное число монеток,
# которые нужно перевернуть, чтобы все монетки были повернуты вверх
# одной и той же стороной. Выведите минимальное количество монет,
# которые нужно перевернуть

n = int(input("Введите число монет: "))
count_no = 0
count_yes = 0
for x in range(n):
    print("Монета ", x+1,  "лежит решкой вверх? (Да, Нет) - ")
    answer = input()
    if answer == "Нет" or answer == "нет":
        count_no += 1
    elif answer == "Да" or answer == "да":
        count_yes += 1
    else:
        answer = input("Некорректный ввод. Введите 'Да' или 'Нет' - ")

print(count_no)
print(count_yes)
if count_no < count_yes:
    result = count_no
else:
    result = count_yes

print("Минимальное количество монет, которые нужно перевернуть: ", result)