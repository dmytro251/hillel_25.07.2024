import string


def popular_words (text: str, words: list[str]) -> dict[str:int]:
    for signs in string.punctuation:
        if signs in text:
            text = text.replace(signs, "")

    list_text = text.lower().split()
    dict_final = {}

    for word in words:
        dict_final.setdefault(word, 0)
        dict_final[word] = list_text.count(word)
    return dict_final


assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')