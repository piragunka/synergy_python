def count_zeros():
    N = int(input("Введите количество чисел N: "))
    count = 0
    print("Введите ровно N целых чисел:")
    for _ in range(N):
        num = int(input())
        if num == 0:
            count += 1
    print("Количество нулей среди введенных чисел:", count)

count_zeros()
