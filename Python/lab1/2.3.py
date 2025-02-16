n = int(input("Введите натуральное число n: "))
num_width = len(str(n))
for i in range(n, 0, -1):
    line = ''
    for j in range(1, i+1):
        line += f"{j:>{num_width}}"
    print(line)
