from typing import Optional


def second_index(text:str, some_str:str) -> Optional[int]:
    _index = text.find(some_str)
    _index = text.find(some_str, _index + 1) \
        if text.find(some_str, _index + 1) >= 0 else None
    return _index


assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')
