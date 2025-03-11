def task2():
    with open("numbers.txt", "r") as file:
        numbers = [int(line.strip()) for line in file if line.strip()]

    numbers.sort()
    with open("sorted.txt", "w") as file:
        for num in numbers:
            file.write(str(num) + "\n")

if __name__ == '__main__':
    task2()
