import string


def is_palindrome(text: str) -> bool:
    for signs in string.punctuation:
        if signs in text:
            text = text.replace(signs, "")

    text = text.replace(" ", "").lower()
    return text == text[::-1]


assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")