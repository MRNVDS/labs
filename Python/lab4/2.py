dictionary = {'Hello': 'Hi', 'Bye': 'Goodbye', 'List': 'Array'}
value = input("Введите значение: ")

found = False
for key, val in dictionary.items():
    if str(val) == value:
        print(key)
        found = True
        break

if not found:
    print("Значение не найдено")
