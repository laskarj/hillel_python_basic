"""
Задача 1. 10 баллов

тема Срезы и условие if.

написать программку которая будет состоять из первых двух и последних символов предоставленной строки.

Если длинна строки меньше двух символов напечатать строку типа.

'Ваша строка слишком короткая - СТРОКА ' . Через метод форматирования строк с %.

Входная строка : 'Hillel school'

Результат1 : 'Hiol'

или

Результат2 : 'Ваша строка слишком короткая - и ваша строка'
"""
user_text = input('Pls Enter txt:')
not_result = str()
if len(user_text) >= 2:
    print(user_text[0:2], user_text[-2:])
else:  # TODO: правильно по можно оставить только else #Исправил
    print('Ваша строка слишком короткая:%s' % user_text)

"""
Задача 2. 15 баллов

Написать программу, которая подсчитывает количество символов в строке

и формирует dict в котором key = буква, value= количество их в слове:

Входная строка : 'Hillel school'

Результат :  {'H': 1, 'i': 1, 'l': 3, 'e': 1, ' ': 1, 's': 1, 'c': 1, 'h': 1, 'o': 2}

"""
user_text = list(input('Enter text pls:'))
my_dict = {}

for i in user_text:
    if i in my_dict:
        my_dict[i] += 1  # TODO: как упростить ? += #УПРОСТИЛ
    else:
        my_dict[i] = 1
print(my_dict)


"""
Задача 7. 10 баллов

Написать программу которая данный список кортежей переведет в список списков

Входные данные: [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]

Результат: [[1, 2], [2, 3, 5], [3, 4], [2, 3, 4, 2]]

БЫЛО:
new_tuple = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
new_list = list(new_tuple[0]), list(new_tuple[1]), list(new_tuple[2]), list(new_tuple[3])
new_list = list(new_list) # TODO: переделай хотя бы через цикл ты же незнаешь колличество
print(new_list)
"""

new_tuple = [(1, 2), (2, 3, 5), (3, 4), (2, 3, 4, 2)]
new_list = []
for i in new_tuple:
    new_list.append(list(i))

print(new_list)

"""
Задача 9. 10 баллов

Тема Листы

Даны два списка элементов если хоть один елемент совпадает отпринтить True.

print(Тrue) не слово! а объект подставить.

БЫЛО:
tipe_list_nober_1 = ['apple', 'coffee', 'bread']
tipe_list_nober_2 = ['banana', 'papaya', 'coffee']
reserv_list = []
for i in tipe_list_nober_1:
    for c in tipe_list_nober_2:
        if i == c:
            reserv_list.append(i)
            print(i) # TODO: не то сделал читай задание. Но в целом ок.

"""

tipe_list_number_1 = ['apple', 'coffee', 'bread']
tipe_list_number_2 = ['banana', 'papaya', 'coffee']
for i in tipe_list_number_1:
    if i in tipe_list_number_2:
        print(i, '-->', True)
        