import sys
import json
import csv
import os


def main():
    if len(sys.argv) < 2:
        print("Использование: python json2csv.py <имя_json_файла>")
        sys.exit(1)

    json_file_name = sys.argv[1]

    with open(json_file_name, 'r', encoding='utf-8') as json_file:
        data = json.load(json_file)

    if isinstance(data, list) and len(data) > 0 and isinstance(data[0], dict):
        headers = list(data[0].keys())
    else:
        print("Формат JSON не соответствует ожидаемому списку словарей.")
        sys.exit(1)

    base_name, _ = os.path.splitext(json_file_name)
    csv_file_name = base_name + ".csv"

    with open(csv_file_name, 'w', encoding='utf-8-sig', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=headers)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

    print(f"Файл {csv_file_name} успешно создан.")


if __name__ == "__main__":
    main()


