set_1 = set()
set_2 = set()
n = int(input("Введите кол-во элементов первого множества: "))
m = int(input("Введите кол-во элементов второго множества: "))

for x in range(n):
    print(f"Введите число {x + 1} для первого множества: ", end=' ')
    number = int(input())
    set_1.add(number)

for y in range(m):
    print(f"Введите число {y + 1} для второго множества: ", end=' ')
    number = int(input())
    set_2.add(number)

union_set = set_1.union(set_2)
list_union_set = list(union_set)
list_union_set.sort()
print(list_union_set)