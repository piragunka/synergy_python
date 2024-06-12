import random

def generate_random_matrix(rows, cols, min_value, max_value):
    return [[random.randint(min_value, max_value) for _ in range(cols)] for _ in range(rows)]

def add_matrices(matrix1, matrix2):
    return [[matrix1[i][j] + matrix2[i][j] for j in range(len(matrix1[0]))] for i in range(len(matrix1))]

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Ошибка: введите целое число. Пожалуйста, попробуйте снова.")

rows = get_int_input("Введите количество строк матрицы: ")
cols = get_int_input("Введите количество столбцов матрицы: ")
min_value = get_int_input("Введите минимальное значение для элементов матрицы: ")
max_value = get_int_input("Введите максимальное значение для элементов матрицы: ")

# Генерация двух матриц с заданными параметрами
matrix_1 = generate_random_matrix(rows, cols, min_value, max_value)
matrix_2 = generate_random_matrix(rows, cols, min_value, max_value)

# Сложение двух матриц
matrix_3 = add_matrices(matrix_1, matrix_2)

print("Matrix 1:")
for row in matrix_1:
    print(row)

print("\nMatrix 2:")
for row in matrix_2:
    print(row)

print("\nMatrix 3 (result of addition):")
for row in matrix_3:
    print(row)
