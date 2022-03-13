"""Скинуть файлик с примерами всех конструкций КРОМЕ менеджера контекста. With/as. 20 баллов"""

my_dict = {"a": 1, "b": 2, "c": 3}

try:
    value = my_dict["a"]
except KeyError:
    print("A KeyError occurred!")
finally:
    print("The finally statement ran!")


def fetcher(obj, index):
    return obj[index]


x = 'spam'

fetcher(x, 3)  # Все равно что x[3].
fetcher(x, 4)  # Обработчик по умолчанию - интерактивная оболочка, возбкждает исключение IndexError.


try:
    fetcher(x, 4)
except IndexError:  # Перехватывает и обрабатывает искдючение.
    print('Got exception ')


def catcher():
    try:
        fetcher(x, 4)
    except IndexError:
        print('Got exception')
    print('continuing')


catcher()

try:
    raise IndexError  # Возбкждает исключение вручную
except IndexError:
    print('Got exception')


# assert False, 'Nobody expects the Spanish Inquisition!'
"""Исключения, определяемые пользователем """


class Bad(Exception):  # Пользовательское исключение
    pass


def doomed():
    raise Bad()  # Возбудит экземпляр исключения


try:
    doomed()
except Bad:  # Перехватить исключение по имени класса
    print('Got Bad')

"""Заключительные операции"""


try:
    fetcher(x, 4)
finally:  # Заключительные операции
    print('after fetch')


def after():
    try:
        fetcher(x, 4)
    finally:
        print('after fetch')
    print('after try?')


after()
