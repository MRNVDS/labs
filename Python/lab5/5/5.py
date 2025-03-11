import os
import argparse


def task5():
    parser = argparse.ArgumentParser(description="Проверка наличия файлов в папке.")
    parser.add_argument("--dirpath", type=str, default=".", help="Путь к папке (по умолчанию текущая)")
    parser.add_argument("--files", nargs="*", help="Имена файлов для проверки")
    args = parser.parse_args()

    dirpath = args.dirpath
    files = args.files

    if files:
        present = []
        absent = []
        for filename in files:
            full_path = os.path.join(dirpath, filename)
            if os.path.isfile(full_path):
                present.append(filename)
            else:
                absent.append(filename)
        with open("present_files.txt", "w", encoding="utf-8") as f:
            for name in present:
                f.write(name + "\n")
        with open("absent_files.txt", "w", encoding="utf-8") as f:
            for name in absent:
                f.write(name + "\n")

        print("Файлы, присутствующие в папке:")
        for name in present:
            print(name)
        print("\nФайлы, отсутствующие в папке:")
        for name in absent:
            print(name)
    else:
        total_files = 0
        total_size = 0
        for item in os.listdir(dirpath):
            full_path = os.path.join(dirpath, item)
            if os.path.isfile(full_path):
                total_files += 1
                total_size += os.path.getsize(full_path)
        print(f"Количество файлов в папке: {total_files}")
        print(f"Общий размер файлов: {total_size} байт")


if __name__ == '__main__':
    task5()
