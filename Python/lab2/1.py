def encode_string(s):
    result = ''
    i = 0
    while i < len(s):
        count = 1
        current_char = s[i]
        while i + 1 < len(s) and s[i + 1] == current_char:
            count += 1
            i += 1
        if count > 1:
            result += f"{current_char}{count}"
        else:
            result += current_char
        i += 1
    return result

input_string = input("Введите строку для кодирования: ")

encoded_string = encode_string(input_string)
print("Закодированная строка:", encoded_string)