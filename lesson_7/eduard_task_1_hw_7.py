#1) 5 примеров list comprehension
list_1 = [i*2 for i in range(10) if i > 2]
print(list_1)

numbers_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list_2 = [i**2 for i in numbers_list if i % 2 == 0]
print(list_2)


list_3 = [i for i in list(zip(numbers_list, list_1))]
print(list_3)

name_list = ['Ruslan', 'Victoria', 'Artur', 'Vasya']
list_4 = [element for element in name_list]
print(list_4)

list_5 = [letter for word in name_list for letter in word]
print(list_5)

#2) 5 examples with DICT comprehension
#1
dict_keys = [1, 10, 100, 1000]
dict_1 = {i: i for i in dict_keys}
print(dict_1)
#2
dict_2 = {num: num * num for num in range(10, 30) if num % 3 == 0}
print(dict_2)
#3
blahs = [('blah0', 'blah'), ('blah1', 'blah'), ('blah2', 'blah'), ('blah3', 'blah')]
dict_3 = {k: v for k, v in blahs}
print(dict_3)
#4
weather_list = ['rain', 'heat', 'cold']
element_list = ['water', 'fire', 'snow']
dict_4 = {k: v for k, v in zip(weather_list, element_list)}
print(dict_4)
#5
d = {'key1': {'a', 'b', 'c'}, 'key2': {'so', 'sad'}, 'key3': {'so', 'sad'}}
dout = {f"a_in_values_of_{k}" if 'a' in v else f"a_not_in_values_of_{k}": v for k, v in d.items()}
print(dout)

#3) 5 примеров с set comprehensions
#1
set_compr_1 = set(item for value in dout.values() for item in value)
print(set_compr_1)
#2
set_compr_2 = set(x for i in blahs for x in i)
print(set_compr_2)
#3
set_compr_3 = set(x for x in range(1, 20) if x % 2 == 0)
print(set_compr_3)
#4
set_compr_4 = set(x for x in [1, 1, 2, 1, 1, 2, 2])
print(set_compr_4)
#5
str_from_cat = 'The cat in the hat had two helpers: one and two'
set_compr_5 = set(word for word in str_from_cat.split() if len(word) <= 3)
print(set_compr_5)
