import codecs


def delete_html_tags(html_file, result_file='cleaned.txt'):
    with codecs.open(html_file, 'r', 'utf-8') as file_r:
        html = file_r.read()

    with open(result_file, 'w') as file_w:
        start_ = 0
        text = ""

        for index, element in enumerate(html):
            if element == ">":
                start_ = index + 1
            elif element == "<":
                text += html[start_:index]
                text = text.strip() + "\n"

        lst_text = text.splitlines()

        for line in lst_text:
            if line.find(" ") == -1 or lst_text.count(line) > 1 :
                lst_text.remove(line)
        file_w.write("\n".join(lst_text))
    return  result_file


with codecs.open(delete_html_tags('draft.html'), 'r') as file:
    print(file.read())
