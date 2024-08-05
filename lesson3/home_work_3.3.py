lst = [1, 2, 3, 4, 5,9]
size = len(lst)
if not size:
    lst_2 = []
    lst_3 = []
    lst_final = lst_2 + lst_3
    print(lst_2)
    print(lst_3)
    print(lst_final)
elif not size % 2:
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
