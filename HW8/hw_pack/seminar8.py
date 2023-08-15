"""
Задание №1
Вспоминаем задачу 3 из прошлого семинара. Мы сформировали
текстовый файл с псевдо именами и произведением чисел.
Напишите функцию, которая создаёт из созданного ранее
файла новый с данными в формате JSON.
Имена пишите с большой буквы.
Каждую пару сохраняйте с новой строки.

"""

import json


def convert(file_name: str) -> None:
    dic = {}
    with open(file_name, 'r', encoding='utf-8') as f:
        for line in f:
            li = line.split(',')  # получили каждый элемент
            dic[li[0].capitalize()] = float(li[1])  # берем первый элемент из словаря
        # print(dict)

        with open('file_json.json', 'w', encoding='utf-8') as f:
            json.dump(dic, f, ensure_ascii=False, indent=2)


convert('new_file.txt')