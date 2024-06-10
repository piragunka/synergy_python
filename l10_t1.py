def age_format(age):
    """ Функция для форматирования возраста с правильным окончанием. """
    if age % 10 == 1 and age % 100 != 11:
        return f"{age} год"
    elif 2 <= age % 10 <= 4 and (age % 100 < 10 or age % 100 > 20):
        return f"{age} года"
    else:
        return f"{age} лет"

def add_pet(pets):
    """ Функция для добавления питомца в словарь. """
    pet_name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = int(input("Введите возраст питомца: "))
    owner_name = input("Введите имя владельца питомца: ")
    
    pets[pet_name] = {
        "Вид питомца": pet_type,
        "Возраст питомца": pet_age,
        "Имя владельца": owner_name
    }

def display_pets(pets):
    """ Функция для отображения информации о всех питомцах. """
    for pet_name, details in pets.items():
        print(f'Это {details["Вид питомца"]} по кличке "{pet_name}". '
              f'Возраст питомца: {age_format(details["Возраст питомца"])}. '
              f'Имя владельца: {details["Имя владельца"]}.')

# Создание пустого словаря для хранения информации о питомцах
pets = {}

# Добавление питомцев в словарь
add_pet(pets)

# Вывод информации о питомцах
display_pets(pets)
