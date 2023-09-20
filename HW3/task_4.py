"""✔ Три друга взяли вещи в поход. Сформируйте
словарь, где ключ — имя друга, а значение —
кортеж вещей. Ответьте на вопросы:
✔ Какие вещи взяли все три друга
✔ Какие вещи уникальны, есть только у одного друга
✔ Какие вещи есть у всех друзей кроме одного
и имя того, у кого данная вещь отсутствует
✔ Для решения используйте операции
с множествами. Код должен расширяться
на любое большее количество друзей."""

peopls = {
    'Женя': ('нож', 'палатка', 'спички', 'спальник', 'вода', 'двора'),
    'Маша': ('кастрюлька', 'спальник', 'удочка', 'фонарик', 'вода'),
    'Майя': ('еда', 'удочка', 'спальник', 'лопата', 'розжиг', 'нож'),
}

all = set()
uniq = set()
two = set()

for people, items in peopls.items():
    all.update(items)
    for item in items:
        if sum(item in people_items for people_items in peopls.values()) == 1:
            uniq.add(item)
        elif sum(item in people_items for people_items in peopls.values()) == 2:
            two.add(item)

common_set = set.intersection(*map(set, peopls.values()))

print(f'Какие вещи взяли все три друга: {common_set}')
print(f'Уникальные вещи, которые есть только у одного: {uniq}')

for item in two:
    for people, items in peopls.items():
        if item not in items:
            print(f'Какие вещи имеют все друзья, но не {people}: {item}')
