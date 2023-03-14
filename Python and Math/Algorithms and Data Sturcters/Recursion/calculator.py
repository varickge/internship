def add_numbers():
    print("Enter the first number:")
    number1=input()

    print("Enter the second number:")
    number2=input()

    print(float(number1)+float(number2))

def subtract_numbers():
    print("Enter the first number:")
    number1 = input()

    print("Enter the second number:")
    number2 = input()

    print(float(number1) - float(number2))

def display_menu():
    print("--> Chose the operation <--")
    print("1. Add numbers")
    print("2. Subtract numbers")

    operation=input()

    if operation=="1":
        return add_numbers()
    elif operation=="2":
        return subtract_numbers()
    else:
        print("Wrong operation entered,please try again")
        display_menu()

display_menu()