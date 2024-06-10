def check_repeats(input_string):
    numbers = input_string.split()
    seen_numbers = set()
    results = []

    for number in numbers:
        if number in seen_numbers:
            results.append("YES")
        else:
            results.append("NO")
            seen_numbers.add(number)
    
    return results

# Цикл для многократного ввода и обработки данных
while True:
    input_string = input("Введите числа через пробел (или введите 'exit' для выхода): ")
    if input_string.lower() == 'exit':
        break
    results = check_repeats(input_string)
    for result in results:
        print(result)
