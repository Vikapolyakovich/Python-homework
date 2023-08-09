def print_operation_table(operation, num_rows=6, num_columns=6):
    list_element = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    print(list_element)
    for i in list_element:
        for j in i:
            print(j, "\t", end=' ')
        print()


print_operation_table(lambda x, y: x * y)