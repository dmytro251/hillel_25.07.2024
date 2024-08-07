main_list = []
first_list = []
second_list = []
final_list = []

if not len(main_list):
    final_list.append(first_list)
    final_list.append(second_list)
    print(final_list)

elif not len(main_list) % 2:
    first_list = main_list[:len(main_list)//2]
    second_list = main_list[len(main_list)//2:]
    final_list.append(first_list)
    final_list.append(second_list)
    print(final_list)

else:
    first_list = main_list[:len(main_list)//2+1]
    second_list = main_list[len(main_list)//2+1:]
    final_list.append(first_list)
    final_list.append(second_list)
    print(final_list)