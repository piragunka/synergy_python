def is_palindrome(s):
    return s == s[::-1]

def main():
    string = input("Введите строку без пробелов: ")
    if is_palindrome(string):
        print("yes")
    else:
        print("no")

main()
