def print_even_numbers(A, B):
    for num in range(A, B + 1):
        if num % 2 == 0:
            print(num, end=' ')

# Вводим A и B
A = int(input("Введите целое число A: "))
B = int(input("Введите целое число B (A ≤ B): "))

# Печатаем четные числа на отрезке [A, B]
print("Четные числа на отрезке [{}, {}]: ".format(A, B))
print_even_numbers(A, B)
