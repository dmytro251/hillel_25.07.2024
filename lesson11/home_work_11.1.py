from inspect import isgenerator


def prime_generator(end: int) -> int:
    count = 2
    while count <= end:
        if count % 2 != 0 and count % 3 != 0 and count % 5 != 0 or count == 2 or count == 3 or count == 5:
            yield count
        count += 1


gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')