number_one = int(input("Введіть першу цифру: "))
number_two = int(input("Введіть другу цифру: "))
operation = input("Виберіть операцію(+,-,*,/):")
if operation == ("+") :
        suma = number_one + number_two
        print(f"{number_one}+{number_two}={suma}")
else:
    if operation == "-":
        vid = number_one - number_two
        print(f"{number_one}-{number_two}={vid}")
    else:
        if operation == "*":
            mn = number_one * number_two
            print(f"{number_one}*{number_two}={mn}")
        else:
            if operation == "/" and number_two == 0 :
                 print("Ділення на нуль не можливе")
            else:
                if operation == "/":
                    dil = number_one / number_two
                    print(f"{number_one}/{number_two}={dil}")
                else:
                    print("Дія не можлива")

