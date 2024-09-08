def is_even(number: int) -> bool:
    even_numbers = ["2", "4", "6", "8", "0"]
    string_numder = str(number)
    return string_numder[-1] in even_numbers


assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'