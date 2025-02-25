def task_1(numbers):
    max_val = max(numbers)
    min_val = min(numbers)
    max_index = numbers.index(max_val)
    min_index = numbers.index(min_val)

    numbers[max_index], numbers[min_index] = numbers[min_index], numbers[max_index]
    return numbers

numbers = list(map(int, input("Введите числа через пробел: ").split()))
print(task_1(numbers))
