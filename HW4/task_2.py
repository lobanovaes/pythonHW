"""
Напишите функцию принимающую на вход только ключевые параметры и
возвращающую словарь, где ключ — значение переданного аргумента,
а значение — имя аргумента.
Если ключ не хешируем, используйте его строковое представление.

"""
def hashable_dicts(**kwargs):
    res = dict()
    for k, v in kwargs.items():
        if isinstance(v, (list, dict, set, bytearray)):
            v = str(v)
        res[v] = k
    return res


print(hashable_dicts(a='mother', b='father', c='baby'))
