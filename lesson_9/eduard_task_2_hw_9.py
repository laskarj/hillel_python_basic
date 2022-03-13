"""
Задача 1. 10 баллов

Написать функцию которая будет добовлять код страны

к номеру телефона с помощью замыкания

внешний вид вызова функции.

my_number = user_telephone('+044')

my_number('838372893')

+044838372893 результат.
"""


def user_telephone(arg1: str):

    def telephone_number(arg2: str):
        print(arg1 + arg2)
    return telephone_number


my_number = user_telephone('+044')
my_number('838372893')

"""
Задача 2. 20 баллов
Написать функцию которая будет у пользователя брать python обект в любом виде и выводить все его не магические методы в 
списке.
и написать декторатор который будет выводить колличество методов в объекте.
Похожую задачу мы уже решали. Можете взять решение из предыдущей . Но декоратор уже ваш полностью)

func(tuple())
[count, index]

@methods_amount
[count, index]
2


Задача 3
Дописать декоратор, чтобы он принимал аргумент, например текст и выводил его тоже
@method_amount(need_to_learn)
[count, index]
'need_to_learn 2'
"""
"""2 и 3 в одном задании"""


def decor_func_arg(args1: str):
    """Еще одна обертка для функции декоратора"""
    def methods_amount(function):
        """Принимает функцию"""
        def inner(*args):
            """Принимает аргументы функции"""
            len_methods = len(function(*args))
            return print(args1, len_methods)
        return inner
    return methods_amount


@decor_func_arg('need to learn')
def func_for_dir(met):
    dir_for_set = dir(met)
    set_method = []
    for i in dir_for_set:
        if not i.startswith('__'):
            set_method.append(i)
    print(set_method)
    return set_method


func_for_dir(tuple)
func_for_dir(str)


"""
Задача 4. 30 баллов
Ваша задача - создать декоратор для функции, которая принимает неограниченное количество позиционных ХЕШИРУЕМЫХ 
элементов.
Декоратор добавляет следующий функционал:
Если функция уже вызвалась с такими аргументами - ваша функция должна вернуть результат выполнения этой функции 
из памяти, а не вычислять его заного.
Если не вызывалась - вычислить результат, положить его в память, и вернуть.
Подсказка - тут вам пригодятся словари.
"""


def cache_function_dec(function):
    """Я пытался долго понять как сделать так чтобы вызывалось значение функции из кэша если поменять позиции аргумента
    но так и не разобрался, в таком виде отправляю потому что и так сильно задержал д.з и уже штраф
    постараюсь разобрать еще"""
    memo = {}

    def elem_func_hash(*args):
        if args in memo:
            return print(f'Эта функция уже вызывалась с такими аргументами вот их значение:{memo[args]}')
        else:
            memo[args] = function(*args)
        return print(f'Значение функции добавлена:{memo[args]}')

    return elem_func_hash


@cache_function_dec
def hash_function(*args: hash):
    if '__hash__' in dir(args):
        dict_i = {v: hash(v) for v in args}
        return dict_i


hash_function('qwerty', 'hello')
hash_function('qwerty', 'hello')
