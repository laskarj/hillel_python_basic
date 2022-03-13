import webbrowser
"""
Найти официальную документацию по Словарям и прикрепить ссылку к домашней работе 5 points
И попробовать прочитать ).
"""
webbrowser.open_new("https://docs.python.org/3.10/library/stdtypes.html#typesmapping")
"""
Task 1. 5 points
сложить словари в один.
использовать for и dict methods.
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
"""
first = {1: 10, 2: 20}
second = {3: 30, 4: 40}
third = {5: 50, 6: 60}
fourth = {7: 70, 8: 80}
fifth = {9: 90, 10: 100}
zip_dict = zip(first.items(), second.items(), third.items(), fourth.items(), fifth.items())
other_dict = dict()
for i in list(zip_dict):
    for k, v in i:
        other_dict[k] = v
print(other_dict)

"""
Task 2. 10 points
1. Создать словарь с ключами от 11 до 20 включительно. Значения = квадраты ключей
2. просуммировать все значения(values), делается в одну строку.(look build in functions)
"""
new_dict = {x: x**2 for x in range(11, 21)}

total_value = 0
for v in new_dict.values():
    total_value += v

print(new_dict)
print(total_value)
"""
Task3. 5 points
отсортировать словарь по ключам
"""
arbitrary_dict = {'jaja': 1, 'tata': 2, 'popo': 3, 'qui': 4}
list_key = list(arbitrary_dict.keys())
list_key.sort()
for i in list_key:
    print(i, ':', arbitrary_dict[i])

"""
Task 4. 15
Удалить дубликаты из dictionary
"""
dictionary_school = \
    {'id1':
        {'name': 'Ruslan', 'class': 1, 'subjects':
            {'Math', 'Algorithms', 'English'}},
     'id2':
        {'name': 'Mark', 'class': 2, 'subjects':
            {'Geometry', 'Java', 'Cooking'}},
     'id3':
        {'name': 'Ruslan', 'class': 1, 'subjects':
            {'Math', 'Algorithms', 'English'}}}

not_double = {}

for k, v in dictionary_school.items():
    if v not in not_double.values():
        not_double[k] = v

print(not_double)


"""
Task 5. 10
вернуть из dictionary все уникальные values.
"""
first_dict =\
    [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]

set_value = set(values for d in first_dict for values in d.values())
print(set_value)

"""
Task 6. 15 Посчитать общее количество наименований в списке. И только в списках.
"""
shedule = {
    'monday': ['clean house', 'drive car', 'meet with freands'],
    'thuesday': None, 'wednesday': ['manicure', 'hammam', 'beer']
          }
list_no_none = []
for i in shedule.values():
    if i:
        for v in i:
            list_no_none.append(v)
print(len(list_no_none))
