import string

variable_name = input("Enter a name for the variable: ")

for index, signs in enumerate(variable_name):
    if signs in string.punctuation:
        variable_name = variable_name.replace(signs, "")

finish_name = variable_name.title()
finish_name = finish_name.replace(" ", "")

if len(finish_name) > 139:
    print(f"#{finish_name[:139]}")
else:
    print(f"#{finish_name}")
