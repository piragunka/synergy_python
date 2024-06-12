def factorial(n):
    if n == 0:
        return 1
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def factorial_sequence(n):
    fact_n = factorial(n)
    result = []
    for i in range(fact_n, 0, -1):
        result.append(factorial(i))
    return result

def get_natural_number():
    while True:
        try:
            user_input = int(input("Введите натуральное число (не больше 6): "))
            if user_input < 1:
                print("Ошибка: Введите число больше 0.")
            elif user_input > 6:
                print("Предупреждение: Ввод числа больше 6 может привести к слишком сложным вычислениям. Пожалуйста, введите число от 1 до 6.")
            else:
                return user_input
        except ValueError:
            print("Ошибка: Введите корректное целое число.")

# Получение ввода от пользователя с проверкой
user_input = get_natural_number()

# Вычисление факториала введенного числа
fact_of_input = factorial(user_input)

# Генерация списка факториалов от факториала введенного числа до 1
resulting_list = factorial_sequence(user_input)

print("Факториал числа", user_input, "равен", fact_of_input)
print("Список факториалов от", fact_of_input, "до 1:", resulting_list)
