lst = [1, 2, 3, 4, 5]
size = len(lst)
if size == 0:
    lst_2 = []
    lst_3 = []
    lst_final = lst_2 + lst_3
    print(lst_2)
    print(lst_3)
    print(lst_final)
elif size % 2 == 0:
    lst_2 = lst[:size // 2]
    lst_3 = lst[size // 2:]
    lst_final = lst_2 + lst_3
    print(lst_2)
    print(lst_3)
    print(lst_final)
else:
    lst_2 = lst[: size // 2 + 1]
    lst_3 = lst[size // 2 + 1:]
    lst_final = lst_2 + lst_3
    print(lst_2)
    print(lst_3)
    print(lst_final)
