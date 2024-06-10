def count_unique_numbers():
    while True:
        N = int(input("Введите количество чисел N (1 ≤ N ≤ 100000): "))
        if 1 <= N <= 100000:
            break
        else:
            print("Ошибка: N должно быть в диапазоне от 1 до 100000.")
    
    while True:
        numbers = list(map(int, input("Введите числа через пробел, каждое число не превышает 2*10^9 по модулю: ").split()))
        if all(abs(num) <= 2*10**9 for num in numbers) and len(numbers) == N:
            break
        else:
            print("Ошибка: Убедитесь, что каждое число не превышает 2*10^9 по модулю и их количество соответствует N.")
    
    unique_numbers = set(numbers)
    
    print("Количество различных чисел среди введенных:", len(unique_numbers))

count_unique_numbers()
