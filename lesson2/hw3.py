while True:
    
    a = float(input("введите первое число: "))
    b = float(input("введите второе число: "))
    operator = input ("введите операнд: ")

    if operator == "=":
        break

    if operator in ('+', '-', '*', '/'):

        if operator == "+":
            rez = a + b
        elif operator == "-":
            rez = a - b
        elif operator == "*":
            rez = a * b
        elif operator == "/":
            if b != 0:
                rez = a / b
            else:
                rez = "Деление на ноль!"
    else:
        print("неверный знак операции!")
    print(f"результат {rez}")
