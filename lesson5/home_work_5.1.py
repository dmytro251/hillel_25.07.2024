import string
import keyword

variable_name = input("Enter a name for the variable: ")

_numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

for signs in variable_name:
    if signs in string.punctuation and signs != "_" or signs == " ":
        print("\nFalse")
        break
    elif variable_name[0] in _numbers:
        print("\nFalse")
        break
    elif variable_name.count("_") == len(variable_name) > 1:
        print("\nFalse")
        break
    elif not variable_name.islower() and variable_name != "_":
        print("\nFalse")
        break
    elif keyword.iskeyword(variable_name):
        print("\nFalse")
        break
    else:
        print("\nTrue")
        break
