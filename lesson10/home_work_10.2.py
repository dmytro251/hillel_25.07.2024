import string


def first_word(text: str) -> str:
    for signs in string.punctuation:

        if signs in text and signs !="'" and signs != ".":
            text = text.replace(signs, "")

    text = text.replace("."," ")
    list_text = text.split()
    result = list_text[0]
#    if list_text[0] != "I" and list_text[0] != "i" and len(list_text[0]) == 1:
#        result = list_text[1]
    return result


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')