from inspect import isgenerator


def pow_(x: int) -> int:
    return x ** 2


def some_gen(begin: int, end: int, func) -> int:
    count = 0
    while count < end:
        yield begin
        begin = func(begin)
        count += 1


gen = some_gen(2, 4, pow_)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')