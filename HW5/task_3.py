"""
Создайте функцию генератор чисел Фибоначчи (см. Википедию).
"""


def fibonacci(n):
    n1, n2 = 0, 1
    print(n1, n2, end=" ")
    for i in range(n + 1):
        yield n1 + n2
        n1, n2 = n2, n1 + n2


print(*fibonacci(10))
