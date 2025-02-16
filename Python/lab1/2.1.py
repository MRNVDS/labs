n = int(input("Введите натуральное число n: "))

for i in range(n, 0, -1):
    line = ''
    for j in range(1, i+1):
        line += str(j)
    print(line)
