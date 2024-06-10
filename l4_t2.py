def calculate_special_number(number):
    num_str = str(abs(number))
    length = len(num_str)
    
    # Извлекаем единицы и десятки
    e = int(num_str[-1])
    d = int(num_str[-2]) if length > 1 else 0
    
    # Извлекаем сотни
    c = int(num_str[-3]) if length > 2 else 0
    
    # Извлекаем тысячи и десятки тысяч
    b = int(num_str[-4]) if length > 3 else 0
    a = int(num_str[-5]) if length > 4 else 0
    
    if a - b == 0:
        return "Division by zero error"
    result = (d ** e) * c / (a - b)
    return result

def main():
    try:
        number = int(input("Введите любое целое число: "))
        result = calculate_special_number(number)
        print("Результат вычислений:", result)
    except ValueError:
        print("Пожалуйста, введите корректное целое число.")
    except Exception as e:
        print("Произошла ошибка:", e)

main()
