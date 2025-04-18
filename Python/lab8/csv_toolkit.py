import csv
import os
import random
import sys

OUTPUT_SEPARATOR = ';'


def read_csv(file_path, separator=','):
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.reader(f, delimiter=separator)
        data = list(reader)
    if not data:
        raise ValueError("Файл пустой")
    header = data[0]
    rows = data[1:]
    return header, rows


def Show(file_path, output_type='top', num=5, separator=','):
    header, rows = read_csv(file_path, separator)
    total = len(rows)
    if total < num:
        print(f"Всего строк данных: {total}. Вывод всех строк, так как их меньше {num}.")
        num_to_show = total
    else:
        num_to_show = num
    if output_type == 'top':
        selected = rows[:num_to_show]
    elif output_type == 'bottom':
        selected = rows[-num_to_show:]
    elif output_type == 'random':
        selected = random.sample(rows, num_to_show)
    else:
        raise ValueError("Неверный параметр output_type. Допустимо 'top', 'bottom', 'random'.")
    widths = [len(str(h)) for h in header]
    for row in selected:
        for i, cell in enumerate(row):
            widths[i] = max(widths[i], len(str(cell)))
    fmt = ' | '.join(f'{{:<{w}}}' for w in widths)
    print(fmt.format(*header))
    print('-+-'.join('-' * w for w in widths))
    for row in selected:
        print(fmt.format(*row))


def Info(file_path, separator=','):
    header, rows = read_csv(file_path, separator)
    num_rows = len(rows)
    num_cols = len(header)
    print(f"{num_rows}x{num_cols}")
    for idx, col_name in enumerate(header):
        values = [row[idx] for row in rows]
        non_empty = [v for v in values if v != '']
        count_non_empty = len(non_empty)
        if non_empty and all(is_int(v) for v in non_empty):
            col_type = 'int'
        elif non_empty and all(is_float(v) for v in non_empty):
            col_type = 'float'
        else:
            col_type = 'string'
        print(f"{col_name}\t{count_non_empty}\t{col_type}")


def is_int(s):
    try:
        int(s)
        return True
    except:
        return False


def is_float(s):
    try:
        float(s)
        return True
    except:
        return False


def DelNaN(file_path, separator=','):
    header, rows = read_csv(file_path, separator)
    clean_rows = [row for row in rows if all(cell != '' for cell in row)]
    return header, clean_rows


def MakeDS(file_path, separator=',', train_ratio=0.7):
    header, rows = read_csv(file_path, separator)
    random.shuffle(rows)
    split_idx = int(len(rows) * train_ratio)
    train = rows[:split_idx]
    test = rows[split_idx:]
    base = os.getcwd()
    work_dir = os.path.join(base, 'workdata')
    learning_dir = os.path.join(work_dir, 'Learning')
    testing_dir = os.path.join(work_dir, 'Testing')
    os.makedirs(learning_dir, exist_ok=True)
    os.makedirs(testing_dir, exist_ok=True)

    def write_csv(path, data_rows):
        with open(path, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f, delimiter=OUTPUT_SEPARATOR)
            writer.writerow(header)
            writer.writerows(data_rows)

    train_path = os.path.join(learning_dir, 'train.csv')
    test_path = os.path.join(testing_dir, 'test.csv')
    write_csv(train_path, train)
    write_csv(test_path, test)
    print(f"Созданы файлы:\n{train_path} ({len(train)} строк)\n{test_path} ({len(test)} строк) с разделителем '{OUTPUT_SEPARATOR}'")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python csv_toolkit.py <путь_к_csv_файлу> [разделитель_для_чтения]")
        sys.exit(1)
    file_path = sys.argv[1]
    sep = sys.argv[2] if len(sys.argv) >= 3 else ','

    print("\n=== Show (первые 5 строк) ===")
    Show(file_path, output_type='top', num=5, separator=sep)

    print("\n=== Info ===")
    Info(file_path, separator=sep)

    print("\n=== DelNaN ===")
    _, rows = read_csv(file_path, sep)
    header, clean_rows = DelNaN(file_path, separator=sep)
    print(f"Строк после удаления с пропусками: {len(clean_rows)} из {len(rows)}")

    print("\n=== MakeDS ===")
    MakeDS(file_path, separator=sep)
