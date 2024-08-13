
while True:
    number_one = int(input("Введіть першу цифру: "))
    number_two = int(input("Введіть другу цифру: "))
    operation = input("Виберіть операцію(+,-,*,/):")

    if operation == "+":
        suma = number_one + number_two
        print(f"\n{number_one}+{number_two}={suma}")
    elif operation == "-":
        vid = number_one - number_two
        print(f"\n{number_one}-{number_two}={vid}")
    elif operation == "*":
        mn = number_one * number_two
        print(f"\n{number_one}*{number_two}={mn}")
    elif operation == "/" and not number_two:
        print("\nДілення на нуль не можливе")
    elif operation == "/":
        dil = number_one / number_two
        print(f"\n{number_one}/{number_two}={dil}")
    else:
        print("\nДія не можлива")

    the_end = input("\nType y to continue or any character to exit: ")
    if the_end != "y" or the_end != "Y":
        break
