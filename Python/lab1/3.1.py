n = int(input("Введите количество строк n: "))

triangle = []

for i in range(n):
    row = [1]
    if i > 0:
        for j in range(1, i):
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)
        row.append(1)
    triangle.append(row)

max_line_length = len('   '.join(map(str, triangle[-1])))

for row in triangle:
    line = '   '.join(map(str, row))
    print(line.center(max_line_length))
