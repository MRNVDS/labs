def task3():
    children = []
    with open("children.txt", "r", encoding="utf-8") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) >= 3:
                last_name, first_name = parts[0], parts[1]
                try:
                    age = int(parts[2])
                    children.append((last_name, first_name, age))
                except ValueError:
                    continue

    if not children:
        print("Нет данных о детях.")
        return

    youngest = min(children, key=lambda x: x[2])
    oldest = max(children, key=lambda x: x[2])

    with open("youngest.txt", "w", encoding="utf-8") as file:
        file.write(f"{youngest[0]} {youngest[1]} {youngest[2]}")
    with open("oldest.txt", "w", encoding="utf-8") as file:
        file.write(f"{oldest[0]} {oldest[1]} {oldest[2]}")


if __name__ == '__main__':
    task3()
