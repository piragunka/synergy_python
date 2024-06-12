class CashRegister:
    def __init__(self):
        self.balance = 0

    def top_up(self, amount):
        if amount < 0:
            raise ValueError("Нельзя пополнить кассу на отрицательную сумму.")
        self.balance += amount
        return f"Касса пополнена на {amount}. Текущий баланс: {self.balance}"

    def count_1000(self):
        thousands = self.balance // 1000
        return f"В кассе {thousands} целых тысяч."

    def take_away(self, amount):
        if amount > self.balance:
            raise ValueError("Недостаточно денег в кассе.")
        self.balance -= amount
        return f"Из кассы забрано {amount}. Текущий баланс: {self.balance}"

# Пример использования класса Касса
cash_register = CashRegister()

# Пополнение кассы
print(cash_register.top_up(5000))

# Подсчет целых тысяч
print(cash_register.count_1000())

# Изъятие денег
print(cash_register.take_away(3000))

# Снова подсчет целых тысяч
print(cash_register.count_1000())

# Попытка забрать больше денег, чем есть
print(cash_register.take_away(3000))  # Ожидается исключение
