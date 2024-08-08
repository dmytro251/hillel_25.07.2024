import random

_list = []
my_list = [random.randint(1, 10) for i in range(random.randint(3, 10))]

_list.append(my_list[0])
_list.append(my_list[2])
_list.append(my_list[-2])

print(my_list)
print(_list)
