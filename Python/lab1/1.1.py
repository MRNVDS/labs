a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

max = a
min = a

if b > max:
    max = b
if c > max:
    max = c

if b < min:
    min = b
if c < min:
    min = c

print("Максимальное число:", max)
print("Минимальное число:", min)
