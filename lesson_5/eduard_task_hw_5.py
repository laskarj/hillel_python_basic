import copy #импортировал для примера copy в Set методах

"""
Задача 1. 10 баллов
пользователь вводит пароль первый раз система запоминает и просит
повторить пароль проверяет его если нет то просит повторить. А если совпал то сообщение.
"""
first_pass = input('Pls enter your password:')
sekond_pass = input('Pls repit your pass:')
if sekond_pass != first_pass:
    sekond_pass = input('Sory, Password is invalid =( re-enter your sekond pass:\n')
    while sekond_pass == first_pass:
        print('Nice to meet you !')
        break
elif sekond_pass == first_pass:
    print('Nice to meet you !')

"""
Задача_2. 5 баллов
Дан список с повторяющимися значениями необходимо из него удалить все определенные значения используя while цикл.
Входные данные: ['bear', 'milk', 'eg', 'eg', 'eg', 'eg'] удалить все eg
Результат: ['bear', 'milk']
"""
data_list = ['bear', 'milk', 'eg', 'eg', 'eg', 'eg']

while 'eg' in data_list:
    data_list.remove('eg')
print(data_list)

"""
Задача_3. 10 баллов
Тема while and else
дан список произвольный с int нужно вывести "all numbers are even" если все четные и NO если нет
Пример входных данных: [11, 23, 65, 44, 76, 533]
Результат: NO
Пример входных данных: [12, 22, 66, 44, 76, 534]
Результат: all numbers are even
"""
#Для меня это было самой тяжелой задачей, голову ломал дней 5:D, Но результатом очень доволен
#Может конечно и не правильно...
enter_number = list(map(int, input('Enter number pls:').split()))
filter_number = [i % 2 == 0 for i in enter_number]
while False in filter_number:
    print('No')
    break
else:
    print('All numbers are even!')


"""
Задача_4 25 баллов
написать программу которая будет создавать список методов из доступных методов питон объектов. Под доступными подразумевается
методы без подчеркиваний
для выполнения нужно понимание разницы copy, deepcopy. Фунции dir()
т.е для объекта set должен быть список методов
['add',
'clear',
'copy',
'difference',
'discard',
'intersection',
'isdisjoint',
'issubset',
'issuperset',
'pop',
'remove',
'union',
'update']
"""
#У меня не только эти методы выводит но и еще по типу difference_update, у них нет перед ними "__" я не знаю магические они или нет
dir_for_set = dir(set)
set_method = []
for i in dir_for_set:
    if not i.startswith('__'):
        set_method.append(i)
print(set_method)

"""
Задача_5 15 баллов

lis + tuple
Прочитать статью и сдать тесты в конце статьи
Set 
прочитать статью и пройти на отлично тест в конце.
"""
#Скрины прилагаются к тестам



"""
Задача_6 5 балллов
Написать примеры всех методов из set объекта.
Пример
set1 = {1,2,3}
# add
set1.add(4)
# update
set1.update([2,3,4,5])
"""
set_1 = {1, 2, 3}
#add
set_1.add(4)
#update
set_1.update([4, 5])
#copy
set_3 = copy.copy(set_1)
#clear
set_3.clear() #set_2 пустой
#difference
set_1.difference(set_3) #Вывод {1,2,3} так как set_2 пустой
#discard
set_1.discard(1) #убираем элемент
#intersection то же что и &
set_2 = {3, 4, 5}
set_1.intersection(set_2)
#isdisjoint
set_1.isdisjoint(set_2) #вывод Folse так как есть 3 и там и там
#remove
set_1.remove(3) #Удаляем 3
#isdisjoint_2
set_1.isdisjoint(set_2) #выведет True так как нет 3
#issubset <= подмножество
set_1.issubset(set_1) #True
#issuperset то же что и >= надмножество
set_1.issuperset(set_2)
#union
set_1.union(set_2) #возвращает набор содержащийся в 2х наборах
#symmetric_difference то же то  и ^:
set_1.symmetric_difference(set_2)
#intersection_update изменяет набор пересичением
set_1.intersection_update(set_2)
#difference_update изменяет набор по разнице переменных -=
set_2.difference_update(set_1)
#symmetric_difference_update изменяет набор симетричной разностью ^=
set_1.symmetric_difference_update(set_2)
#pop
set_1.pop() #Удаляет произвольный элемент


