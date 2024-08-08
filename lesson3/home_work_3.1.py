number_one = int(input("Введіть першу цифру: "))
number_two = int(input("Введіть другу цифру: "))
operation = input("Виберіть операцію(+,-,*,/):")
if operation == "+":
    suma = number_one + number_two
    print(f"{number_one}+{number_two}={suma}")
elif operation == "-":
    vid = number_one - number_two
    print(f"{number_one}-{number_two}={vid}")
elif operation == "*":
    mn = number_one * number_two
    print(f"{number_one}*{number_two}={mn}")
elif operation == "/" and not number_two:
    print("Ділення на нуль не можливе")
elif operation == "/":
    dil = number_one / number_two
    print(f"{number_one}/{number_two}={dil}")
else:
    print("Дія не можлива")
