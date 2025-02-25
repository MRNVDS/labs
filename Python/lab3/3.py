from collections import Counter

def task_3(strings):
    count = Counter(strings)
    result = [count[string] for string in strings]
    return result

strings = input("Введите строки через пробел: ").split()
print(task_3(strings))

