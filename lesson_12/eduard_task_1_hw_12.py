"""Задача 1: 10 баллов написать 3 примера генераторных функций с различными последовательностями."""


# 1: Обход вложеных структур без вложеных цыклов с помощью yield
def chain(*iterables):
    """Появилась привычка забегать на Хабр, там нашел похожий пример с генератором итераторов """
    for it in iterables:
        yield from it


data_value = chain([1, 2, 3], {'A', 'B', 'C'}, '...')

print(list(data_value))

# 2: Обход чисел с помошь yield:


def countdown(n: int):
    while n != 0:
        yield n - 1
        n -= 1


c = countdown(5)
print(next(c))
print(next(c))
print(next(c))
print(next(c))
print(next(c))

# 3


def fib(n: int):
    a = b = 1
    for i in range(n):
        yield i
        a, b = b, a + b


f = fib(10)
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))


