def task1():
    with open("input.txt", "r") as file:
        data = file.read().strip()
    numbers = list(map(float, data.split()))

    product = 1
    for num in numbers:
        product *= num
    with open("output.txt", "w") as file:
        file.write(str(product))

if __name__ == '__main__':
    task1()
