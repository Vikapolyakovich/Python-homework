text = input('Введите текст: ')
list_vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'э', 'ю', 'я']

list_count = []
for x in text.split():
    count = 0
    for y in x:
        if y in list_vowels:
            count += 1
    list_count.append(count)


if list_count.count(list_count[0]) == len(text.split()):
    print("Парам пам-пам")
else:
    print("Пам парам")
