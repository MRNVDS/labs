import os


def task6(target_folder="."):
    absent_file = "absent_files.txt"
    if not os.path.isfile(absent_file):
        print(f"Файл {absent_file} не найден.")
        return

    with open(absent_file, "r", encoding="utf-8") as file:
        filenames = [line.strip() for line in file if line.strip()]
    if not filenames:
        print("Список отсутствующих файлов пуст.")
        return

    for name in filenames:
        full_path = os.path.join(target_folder, name)
        if not os.path.exists(full_path):
            with open(full_path, "w", encoding="utf-8") as f:
                pass

    print("Отсутствующие файлы успешно созданы.")


if __name__ == '__main__':
    import sys

    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    task6(folder)
