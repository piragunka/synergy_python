N = int(input("Введите кол-во элементов в массиве: ").strip())

numbers = []

# Считывание чисел и добавление их в список
for _ in range(N):
    number = int(input("Введите число внутри массива: ").strip())
    numbers.append(number)

# Переворачиваем список
reversed_numbers = numbers[::-1]

print("Ответ: ")
for num in reversed_numbers:
    print(num)
