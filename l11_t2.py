import collections

pets = {
    1: {"Мухтар": {"Вид питомца": "Собака", "Возраст питомца": 9, "Имя владельца": "Павел"}},
    2: {"Каа": {"Вид питомца": "желторотый питон", "Возраст питомца": 19, "Имя владельца": "Саша"}}
}


def get_suffix(age):
    if age % 10 == 1 and age % 100 != 11:
        return "год"
    elif 2 <= age % 10 <= 4 and not (12 <= age % 100 <= 14):
        return "года"
    else:
        return "лет"

def get_pet(ID):
    if ID in pets:
        return pets[ID]
    else:
        return False

def input_int(message):
    while True:
        user_input = input(message)
        try:
            return int(user_input)
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")

def create():
    last = collections.deque(pets, maxlen=1)[0] + 1 if pets else 1
    pet_name = input("Введите кличку питомца: ")
    pet_type = input("Введите вид питомца: ")
    pet_age = input_int("Введите возраст питомца: ")
    owner_name = input("Введите имя владельца питомца: ")

    pets[last] = {pet_name: {"Вид питомца": pet_type, "Возраст питомца": pet_age, "Имя владельца": owner_name}}

def read(ID):
    pet_info = get_pet(ID)
    if pet_info:
        for name, info in pet_info.items():
            print(f'Это {info["Вид питомца"]} по кличке "{name}". Возраст питомца: {info["Возраст питомца"]} {get_suffix(info["Возраст питомца"])}. Имя владельца: {info["Имя владельца"]}.')
    else:
        print("Питомец с таким ID не найден.")

def update(ID):
    if ID in pets:
        pet_name = list(pets[ID].keys())[0]
        print("Текущая информация о питомце:", pets[ID][pet_name])
        pet_type = input("Введите новый вид питомца или нажмите Enter для пропуска: ")
        pet_age = input("Введите новый возраст питомца или нажмите Enter для пропуска: ")
        owner_name = input("Введите новое имя владельца или нажмите Enter для пропуска: ")

        if pet_type:
            pets[ID][pet_name]["Вид питомца"] = pet_type
        if pet_age:
            pets[ID][pet_name]["Возраст питомца"] = input_int("Введите корректный возраст питомца: ")
        if owner_name:
            pets[ID][pet_name]["Имя владельца"] = owner_name
    else:
        print("Питомец с таким ID не найден.")


def delete(ID):
    if ID in pets:
        del pets[ID]
        print("Запись о питомце успешно удалена.")
    else:
        print("Питомец с таким ID не найден.")

def pets_list():
    if pets:
        for ID, pet_info in pets.items():
            for name, info in pet_info.items():
                print(f'ID: {ID}, {name}, Вид: {info["Вид питомца"]}, Возраст: {info["Возраст питомца"]}, Владелец: {info["Имя владельца"]}')
    else:
        print("Список питомцев пуст.")

def main():
    while True:
        command = input("Введите команду (create, read, update, delete, list, stop): ")
        if command == 'stop':
            break
        elif command == 'create':
            create()
        elif command == 'read':
            pet_id = int(input("Введите ID питомца для чтения информации: "))
            read(pet_id)
        elif command == 'update':
            pet_id = int(input("Введите ID питомца для обновления информации: "))
            update(pet_id)
        elif command == 'delete':
            pet_id = int(input("Введите ID питомца для удаления: "))
            delete(pet_id)
        elif command == 'list':
            pets_list()
        else:
            print("Неизвестная команда.")

main()
