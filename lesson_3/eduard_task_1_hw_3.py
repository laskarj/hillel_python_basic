"""
Задача 1 на 10 балов
Спросить у пользователя возраст.
Спомощью if -elif-else
Если 18 лет вывести “Wait a little bit”
Если больше 18 вывести “You are welcome”
Все остальные варианты. Вывести “Go back to school”
"""
#Asking age
age = input("Please enter yuor age:")
#Age-appropriate options
if int(age) == 18:
    print('Wait a little bit!')
elif int(age) >= 18:
    print('You are welcome!')
#No options
else:
    print('Go beck to school!')
