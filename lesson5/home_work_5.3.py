import string

variable_name = input("Enter a name for the variable: ")
finish_name = variable_name.title()

for index, signs in enumerate(variable_name):
    if signs in string.punctuation or signs == " ":
        finish_name = finish_name.replace(signs, '')

if len(finish_name) > 139:
    print(f"#{finish_name[:139]}")
else:
    print(f"#{finish_name}")
