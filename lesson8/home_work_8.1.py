def add_one(some_list: list[int]) -> list[int]:
    number = 0
    for index, element in enumerate(some_list):
        number += element * 10 ** (len(some_list) - index - 1)

    number += 1
    final_lst = list(range(len(str(number))))

    if not number % 10 and number != 0:
        for index, elements in enumerate(final_lst):
            final_lst[index] = number // 10 ** (len(some_list) - index)
            number %= 10 ** (len(some_list) - index)
    else:
        for index, elements in enumerate(final_lst):
            final_lst[index] = number // 10 ** (len(some_list) - index - 1)
            number %= 10 ** (len(some_list) - index - 1)
    return final_lst


assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")