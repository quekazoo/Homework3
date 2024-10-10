first_number = int(input("Введите первое число: "))
operation = input("Введите действие (+, -, *, /): ")
second_number = int(input("Введите второе число: "))
if operation == "+":
    print(first_number + second_number)
elif operation == "-":
    print(first_number - second_number)
elif operation == "*":
    print(first_number * second_number)
elif operation == "/":
    if second_number != 0:
        print(first_number / second_number)
    else:
        print("НА 0 ДЕЛИТЬ НЕЛЬЗЯ!")