def task_2(list1, list2):
    return len(set(list1) & set(list2))

list1 = list(map(int, input("Введите числа для первого списка через пробел: ").split()))
list2 = list(map(int, input("Введите числа для второго списка через пробел: ").split()))

print(task_2(list1, list2))
