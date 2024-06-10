def remove_extra_spaces(string):
    return ' '.join(string.split())

# Пример использования:
input_string = input("Введите строку: ")
result_string = remove_extra_spaces(input_string)
print("Измененная строка:", result_string)
