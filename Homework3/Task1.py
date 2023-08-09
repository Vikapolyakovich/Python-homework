first_element = int(input('Введите первый элемент арифметической прогрессии: '))
difference = int(input('Введите разность: '))
n = int(input('Введите кол-во элементов: '))
array = []

for x in range(1, n+1):
    element = first_element + ((x - 1)*difference)
    array.append(element)


print(array)
