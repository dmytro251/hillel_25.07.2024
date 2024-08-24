import string
import keyword


variable_name = input("Enter a name for the variable: ")
result = "\nTrue"
_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for signs in variable_name:
    if signs in string.punctuation and signs != "_" or signs == " ":
        result = result.replace("True", "False")
        break

if variable_name[0] in _numbers:
    print("\nFalse")
elif variable_name.count("_") == len(variable_name) > 1:
    print("\nFalse")
elif not variable_name.islower() and variable_name != "_":
    print("\nFalse")
elif keyword.iskeyword(variable_name):
    print("\nFalse")
else:
    print(result)

