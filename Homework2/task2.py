bushes = int(input("Введите кол-во кустов: "))
list_berries = []
max_num = 0
for x in range(bushes):
    print(f"Сколько ягод выросло на {x+1} кусте?", end=' ')
    count_of_berries = int(input())
    list_berries.append(count_of_berries)


list_count = []
for i in range(len(list_berries)):
    list_count.append(list_berries[i-2] + list_berries[i-1] + list_berries[i])
print(list_count)
print(max(list_count))
