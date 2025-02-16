from collections import Counter

input_string = input("Введите строку: ")
cleaned_string = input_string.replace(' ', '')
char_count = Counter(cleaned_string)
most_common_chars = char_count.most_common(3)

print("3 наиболее часто встречающихся символа:")
for char, count in most_common_chars:
    print(f"Символ '{char}' встречается {count} раз(а)")
