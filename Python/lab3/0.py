def task_0(numbers):
    result = [numbers[i] for i in range(1, len(numbers)) if numbers[i] > numbers[i-1]]
    return result

numbers = list(map(int, input("Введите числа через пробел: ").split()))
print(task_0(numbers))
