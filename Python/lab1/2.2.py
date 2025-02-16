n = int(input("Введите натуральное число n: "))

for i in range(n, 0, -1):
    spaces = ' ' * (n - i)
    decreasing = ''.join(str(j) for j in range(i, 0, -1))
    increasing = ''.join(str(j) for j in range(2, i+1))
    line = spaces + decreasing + increasing
    print(line)
