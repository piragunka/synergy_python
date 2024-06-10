def min_boats(m, weights):
    weights.sort()
    i, j = 0, len(weights) - 1
    boats = 0
    while i <= j:
        if weights[i] + weights[j] <= m:
            i += 1
        j -= 1
        boats += 1
    return boats

m = int(input("Введите максимальную массу, которую может выдержать одна лодка (m): "))
n = int(input("Введите количество рыбаков (n): "))

weights = []
for i in range(n):
    weight = int(input(f"Введите вес рыбака номер {i+1}: "))
    weights.append(weight)

required_boats = min_boats(m, weights)
print(f"Минимальное количество лодок, необходимое для переправки всех рыбаков: {required_boats}")
