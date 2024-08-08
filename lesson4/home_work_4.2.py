my_list = [0, 1, 7, 2, 4, 8]

if my_list == []:
    print(0)

elif len(my_list) == 1:
    print(my_list[0] ** 2)

else:
    _sum = 0
    for i, el in enumerate(my_list):
        if not i % 2:
            _sum += el
    print(_sum * my_list[-1])
