user_number = int(input("Enter a number: "))
final_number = user_number

numerical_list = list(range(len(str(final_number))))

while final_number>9:
    product = 1
    for i, el in enumerate(numerical_list):
        numerical_list[i] = final_number % 10
        product *= numerical_list[i]
        final_number //= 10
    numerical_list = list(range(len(str(product))))
    final_number += product

print(final_number)
