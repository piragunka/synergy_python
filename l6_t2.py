def count_divisors(x):
    divisors = 0
    i = 1
    while i * i <= x:
        if x % i == 0:
            # Если i квадрат числа, учитываем только один делитель
            if i * i == x:
                divisors += 1
            # Иначе учитываем два делителя: i и x // i
            else:
                divisors += 2
        i += 1
    return divisors

if __name__ == "__main__":
    x = int(input("Введите натуральное число X: "))
    if x <= 0:
        print("Число должно быть натуральным.")
    else:
        print(f"Количество натуральных делителей числа {x}: {count_divisors(x)}")
