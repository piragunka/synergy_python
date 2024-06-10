def describe_number(number):
    if number == 0:
        return "нулевое число"

    sign = "положительное" if number > 0 else "отрицательное"

    if number % 2 == 0:
        return f"{sign} четное число"
    else:
        return "число не является четным"

user_input = input("Введите целое число: ")
try:
    number = int(user_input)
    print(describe_number(number))
except ValueError:
    print("Введенные данные не являются целым числом.")
