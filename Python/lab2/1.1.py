def decode_string(s):
    result = ''
    i = 0
    while i < len(s):
        current_char = s[i]
        i += 1
        count = ''
        while i < len(s) and s[i].isdigit():
            count += s[i]
            i += 1
        if count:
            result += current_char * int(count)
        else:
            result += current_char
    return result

encoded_string = input("Введите закодированную строку для декодирования: ")

decoded_string = decode_string(encoded_string)
print("Декодированная строка:", decoded_string)
