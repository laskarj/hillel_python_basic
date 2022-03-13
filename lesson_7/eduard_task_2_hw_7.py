"""
сделать пример функции
без return c pass or ...
сделать 5 различных функций на свое усмотрение.
"""


def new_func_1():
    """1.1"""
    pass


def new_func_2():
    """"1.2"""
    ...


def func_app_list(*args, new_list=None):
    """2.1:Apend for list in tuple"""
    if not new_list:
        new_list = []
    new_list.append(args)
    return new_list


x = func_app_list('free', 'for', 'nice', 2)
print(x)


def func_from_lutz(arg1: str, arg2: str):
    """2.2: [x for x in arg1 if x in arg2] from Lutz"""
    list_app = []
    for i in arg1:
        if i in arg2:
            list_app.append(i)
    return list_app


test_string_1 = 'build'
test_string_2 = 'brain'

print(func_from_lutz(test_string_1, test_string_2))


def my_decorated_function(*args):
    """2.3 input function"""
    return args


print(my_decorated_function('Kolbaska!'))


def more_then_30(ch: int):
    """2.4 bool for ch > 30)"""
    return ch > 30


print(more_then_30(31))
print(more_then_30(29))


def func_morning(name: str):
    """2.5"""
    return print(f'Hello,{name}!Good morning!')


func_morning('Ruslan')
"""
1) написать функцию которая в качестве аргумента принимает размер стороны квадрата, а возвращает кортеж в котором лежат три значения:
-периметр квадрата 
-диагональ квадрата 
-площадь квадрата 
"""


def square_function(sq: int):
    p = 4 * sq
    d = (2 * (sq * sq)) ** 0.5
    s = sq * sq
    tuple_square = (p, d, s)
    print(tuple_square)
    return tuple_square


square_function(15)

"""
2) написать функцию которая принимает в качестве аргумента номер месяца, в возвращает строку - время года, этого месяца
"""


def func_in_month(number: int):
    dict_season = {'winter': [1, 2, 12], 'spring': [3, 4, 5], 'summer': [6, 7, 8], 'autumn': [9, 10, 11]}
    for k, v in dict_season.items():
        for i in v:
            if i == number:
                return print(k)


func_in_month(12)
func_in_month(5)
func_in_month(7)
func_in_month(10)

"""
3) написать функцию, которая принимает в качестве аргументов два списка, а возвращает список, 
состоящий из элементов этих двух списков, при чем: 
первый элемент списка - первый элемент первого аргумента, 
второй элемент списка - первый элемент второго списка, 
третий элемент - второй элемент первого списка, 
четвертый - второй элемент второго аргумента и т.д.

т.е для аргументов [1, 2, 3] и [11, 22, 33] функция должна вернуть [1, 11, 2, 22, 3, 33].
Будет плюсом использование генераторов последовательностей для решения этой задачи.
"""


def function_list(args1: list, args2: list):
    """Программа с помощью Зипа склеивает элементы в таплы, при этом склеивает по элементно из каждого списка
    и потом создаем с помошью понимания списка список элементов из кортежей"""
    global_list_1 = list(zip(args1, args2))
    global_list_2 = [i for d in global_list_1 for i in d]
    print(global_list_2)
    return global_list_2


function_list([1, 2, 3, 4], [11, 22, 33, 44])


"""
4) Написать функцию которая принимает в качестве аргумента строку, и возвращает True,
если строка является полиндромом и False если нет.
"""


def poli_func(args: str):
    args = args.replace(' ', '').lower()
    if args == args[::-1]:
        print(True)
    else:
        print(False)
    return


poli_func("saippuakivikauppias")  #Между прочим это самый длинный полиндром в мире в переводе продавец мыла
poli_func("а роза упала на лапу Азора") #Ну чтобы наверняка и самая длинная фраза

