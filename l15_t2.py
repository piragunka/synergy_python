class Transport:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Autobus(Transport):
    pass  # Так как мы только наследуем без добавления новых свойств или методов

# Создание объекта Autobus
bus = Autobus("Renaul Logan", 180, 12)

# Вывод информации об автобусе
print(f"Название автомобиля: {bus.name} Скорость: {bus.max_speed} Пробег: {bus.mileage}")
