def investment_decision(min_investment, michael_funds, ivan_funds):
    michael_can_invest = michael_funds >= min_investment
    ivan_can_invest = ivan_funds >= min_investment
    combined_funds = michael_funds + ivan_funds

    if michael_can_invest and ivan_can_invest:
        return 2
    elif michael_can_invest:
        return "Mike"
    elif ivan_can_invest:
        return "Ivan"
    elif combined_funds >= min_investment:
        return 1
    else:
        return 0

# Ввод значений
min_investment = float(input("Введите минимальную сумму инвестиций: "))
michael_funds = float(input("Сколько денег у Майкла? "))
ivan_funds = float(input("Сколько денег у Ивана? "))

# Решение, основанное на введенных данных
result = investment_decision(min_investment, michael_funds, ivan_funds)

# Вывод результата
print(result)
