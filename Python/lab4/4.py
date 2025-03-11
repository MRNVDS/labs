from collections import Counter

def top_three_digits(s):
    digits = [int(ch) for ch in s if ch.isdigit()]
    counts = Counter(digits)
    top_three = counts.most_common(3)
    result = {num: count for num, count in top_three}
    return result

s = input("Введите строку с цифрами: ")
print(top_three_digits(s))
