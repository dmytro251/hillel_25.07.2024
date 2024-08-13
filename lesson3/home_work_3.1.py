
while True:
    number_one = int(input("Введіть першу цифру: "))
    number_two = int(input("Введіть другу цифру: "))
    operation = input("Виберіть операцію(+,-,*,/):")

    if operation == "+":
        _sum = number_one + number_two
        print(f"\n{number_one}+{number_two}={_sum}")
    elif operation == "-":
        difference = number_one - number_two
        print(f"\n{number_one}-{number_two}={difference}")
    elif operation == "*":
        product = number_one * number_two
        print(f"\n{number_one}*{number_two}={product}")
    elif operation == "/" and not number_two:
        print("\nДілення на нуль не можливе")
    elif operation == "/":
        fraction = number_one / number_two
        print(f"\n{number_one}/{number_two}={fraction}")
    else:
        print("\nДія не можлива")

    the_end = input("\nType y to continue or any character to exit: ")
    if the_end != "y" or the_end != "Y":
        break
