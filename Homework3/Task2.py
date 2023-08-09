n = int(input('Введите кол-во элементов в массиве: '))
print('Введите массив чисел ')
array = []
for x in range(n):
    element = int(input('Введите число: '))
    array.append(element)

min = int(input('Введите минимально заданное число в диапазоне: '))
max = int(input('Введите максимально заданное число в диапазоне: '))

for x in range(1, len(array)):
    if array[x]>= min and array[x]<=max:
        print(x, end=' ')


