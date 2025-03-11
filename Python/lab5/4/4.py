import os
import shutil

def task4(folder_path):
    current_script = os.path.abspath(__file__)
    files_smaller_than_2k = []

    for item in os.listdir(folder_path):
        full_path = os.path.join(folder_path, item)
        if os.path.abspath(full_path) == current_script:
            continue
        if os.path.isfile(full_path) and os.path.getsize(full_path) < 2048:
            files_smaller_than_2k.append(item)

    if files_smaller_than_2k:
        print("Найденные файлы меньше 2К:")
        for filename in files_smaller_than_2k:
            print(filename)

        small_dir = os.path.join(folder_path, "small")
        if not os.path.exists(small_dir):
            os.mkdir(small_dir)

        for filename in files_smaller_than_2k:
            src = os.path.join(folder_path, filename)
            dst = os.path.join(small_dir, filename)
            shutil.copy(src, dst)
    else:
        print("Нет файлов меньше 2К.")


if __name__ == '__main__':
    specific_path = r"C:\Users\Pingv\PycharmProjects\labspython\.venv\Python\lab5\4\test_folder"
    task4(specific_path)
