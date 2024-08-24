
while True:
    number_one = int(input("Enter the first number: "))
    number_two = int(input("Enter the second number: "))
    operation = input("Select an operation(+,-,*,/):")

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
        print("\nDivision by zero is not possible")
    elif operation == "/":
        fraction = number_one / number_two
        print(f"\n{number_one}/{number_two}={fraction}")
    else:
        print("\nAction is not possible")

    the_end = input("\nType y to continue or any character to exit: ")
    if the_end != "y" and the_end != "Y":
        break
