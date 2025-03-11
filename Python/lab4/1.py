dictionary = {'Hello': 'Hi', 'Bye': 'Goodbye', 'List': 'Array'}
key = input("Введите ключ: ")

if key in dictionary:
    print(dictionary[key])
else:
    print("Ключ не найден")
