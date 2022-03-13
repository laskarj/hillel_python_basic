"""
Задача 20 баллов написать функцию которая принимает от пользователя 2 аргумента и делит онин на другой.
при попытке деления на ноль вывести пользователю "ай яй яй делить на ноль можно не многим"
Все остальные исключения с поймать и вывести их значение в текстовом формате.
И в любом случае вывести. " I 'am happy that you learn python"
"""


def divide(arg1: int, arg2: int):
    try:
        result = arg1 // arg2
        return print(result)
    except ZeroDivisionError:
        print('ай яй яй делить на ноль можно не многим')
    except BaseException as e:
        print(e)
    finally:
        print(" I\'am happy that you learn python")


divide(10, 0)
divide('eqw', 2)
