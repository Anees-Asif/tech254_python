def add(int1, int2):
    return int1 + int2


def sub(int1, int2):
    return int1 - int2


def mult(int1, int2):
    return int1 * int2


def div(int1, int2):
    return int1 / int2


while True:
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    user_choice = int(input("Choose an option: "))
    if user_choice == 5:
        print("Exiting")
        break
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if user_choice == 1:
        print(add(num1, num2))
    elif user_choice == 2:
        print(sub(num1, num2))
    elif user_choice == 3:
        print(mult(num1, num2))
    elif user_choice == 4:
        print(div(num1, num2))
    else:
        print("Invalid input. Please enter a valid operation.")
