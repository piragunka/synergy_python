word = input("Введите слово: ")

vowels = 'aeiou'

# Словарь для подсчёта каждой гласной буквы
vowel_counts = {vowel: 0 for vowel in vowels}

vowel_count = 0
consonant_count = 0

for char in word:
    if char in vowels:
        vowel_count += 1
        vowel_counts[char] += 1
    else:
        consonant_count += 1

print(f"Количество гласных букв: {vowel_count}")
print(f"Количество согласных букв: {consonant_count}")
for vowel in vowels:
    if vowel_counts[vowel] == 0:
        print(f"{vowel}: False")
    else:
        print(f"{vowel}: {vowel_counts[vowel]}")
