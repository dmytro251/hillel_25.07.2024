my_list = [2]

if not my_list:
    print(0)

else:
    _sum = 0
    for i, el in enumerate(my_list):
        if not i % 2:
            _sum += el
    print(_sum * my_list[-1])

