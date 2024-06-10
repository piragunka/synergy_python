start = int(input("Введите начальное значение диапазона: "))
end = int(input("Введите конечное значение диапазона: "))

# Определение шага для range в зависимости от порядка значений start и end
step = 1 if start <= end else -1

# Создание словаря с помощью генератора словаря
my_dict = {x: x**x for x in range(start, end + step, step)}

print(my_dict)
