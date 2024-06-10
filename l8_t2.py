def rearrange_array(arr):
    if not arr:
        return arr
    
    last_element = arr[-1] 
    
    for i in range(len(arr) - 1, 0, -1):
        arr[i] = arr[i - 1]
    
    arr[0] = last_element
    return arr

def main():
    n = int(input("Введите количество элементов N: "))
    numbers = list(map(int, input("Введите элементы массива через пробел: ").split()))
    
    if len(numbers) != n:
        print("Количество элементов не соответствует заявленному.")
    else:
        rearranged = rearrange_array(numbers)
        print("Измененный массив:", ' '.join(map(str, rearranged)))

if __name__ == "__main__":
    main()
