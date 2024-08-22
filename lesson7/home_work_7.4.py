def common_elements() -> set:
    list_first = list(range(0,100,3))
    list_seckond = list(range(0,100,5))
    return set(list_first) & (set(list_seckond))


print(common_elements())
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
