import json

from nltk import sent_tokenize
from setuptools._vendor.ordered_set import is_iterable

path_json_out = r"D:\Study\University\Sem 7\КПРС ПО\Лабораторные\5\response.json"

path_json_in = r"D:\Study\University\Sem 7\КПРС ПО\Лабораторные\5\request.json"


def flatten(l):
    """
    Преобразование из списка списков в список
    :param l: список списков
    :return: список
    """
    if is_iterable(l):
        flat = []
        for i in l:
            if is_iterable(i):
                flat.extend(flatten(i))
            else:
                flat.append(i)
        return flat
    return [l]


def open_file(filename):
    """
    Чтение данных с текстового файла
    :param filename: текстовый файл
    :return: список, разбитый на предложения
    """
    with open(filename, encoding='utf-8') as file:
        a = [sent_tokenize(i) for i in file.readlines()]
        return flatten(a)


def read_json(filename_json):
    """
    Чтение данных с json файла
    :param filename_json: json файл
    :return: словарь данных из файла
    """
    with open(filename_json) as json_file:
        return json.load(json_file)


def search_words():
    """
    Основная функция
    :return:
    """
    json_obj = read_json(path_json_in)
    s = json_obj["file name"]
    s = "D:/Study/University/Sem 7/КПРС ПО/Лабораторные/5/" + s
    file_read = open_file(s)

    proposal = []

    for str_read in file_read:
        if json_obj["example minimum length"] <= len(str_read) <= json_obj["example maximum length"]:
            fl_search = True
            for words in json_obj["words"]:
                if words not in str_read:
                    fl_search = False
                    break
            if fl_search:
                proposal.append(str_read)
        if len(proposal) == json_obj["number of examples"]:
            break

    # Запись в файл
    with open(path_json_out, 'w') as json_file:
        if len(proposal) != 0:
            cnt = 1
            data = {}
            for str_s in proposal:
                data[cnt] = str_s
                cnt += 1
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        else:
            json.dump({"Result": "The search failed"}, json_file, indent=4)


search_words()
