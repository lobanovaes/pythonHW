def transparent_matrix(*a_list: list) -> list:
    is_transparent = True
    col = len(a_list[0])
    for a in list(a_list):
        if len(a) != col:
            is_transparent = False
    if is_transparent:
        return list(zip(*a_list))
    else:
        return 'Матрицу нельзя транспорировать'


print(transparent_matrix([9, 3, 5, 9], [2, 7, 4, 6]))
