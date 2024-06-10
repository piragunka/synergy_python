def count_common_numbers():
    import sys
    input = sys.stdin.read
    print("Введите числа первого списка, каждое на новой строке.")
    print("После последнего числа первого списка введите пустую строку, а затем продолжите ввод чисел второго списка.")
    
    data = input().split('\n')
    
    if '' not in data:
        print("Не найдена пустая строка для разделения списков. Убедитесь, что между списками есть пустая строка.")
        return

    index = data.index('')
    list1 = data[:index]
    list2 = data[index+1:]
    
    # Преобразуем списки строк в множества целых чисел
    set1 = set(map(int, list1))
    set2 = set(map(int, list2))
    
    # Найдем пересечение множеств
    common_numbers = set1.intersection(set2)
    
    print(f"Количество общих чисел в обоих списках: {len(common_numbers)}")

print("Добро пожаловать в программу для определения количества общих чисел в двух списках =)")
count_common_numbers()
