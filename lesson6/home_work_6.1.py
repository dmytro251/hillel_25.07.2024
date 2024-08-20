import string

user_letters = input("Enter two letters with a hyphen: ")

symbols_between = string.ascii_letters
index_start = symbols_between.find(user_letters[0])
index_final = symbols_between.find(user_letters[2]) + 1

print("\n",symbols_between[index_start:index_final])
