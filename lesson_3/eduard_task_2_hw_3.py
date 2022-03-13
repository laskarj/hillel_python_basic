"""
Задача 2 на 25 балов
Написать программу, которая:
Приветствует пользователя в произвольном виде.
Принимает на ввод его никнейм, пол, возраст.
Если никнейм содержит admin, выводит: "Привет, повелитель!", не прекращая работу.
Если возраст больше 10 и меньше 14 и пол М или больше 30 и пол М: Выводит "Советую Вам посмотреть "StarWars" или 'Мандалорец'"
Если возраст больше 22 и меньше 32 и пол Ж: Рекомендация "Советую Вам посмотреть "Трансформеры""
Если возраст меньше 16 и пол Ж: Рекомендация "Советую Вам посмотреть "Инсургент""
Если никнейм 'Женя': Рекомендация "Советую Вам посмотреть 'TENET'"
Если возраст до 11 и пол М: Рекомендация "Советую Вам посмотреть "TMNT""
Если никнейм Guido: Кроме рекомендации, выводит "Огромное спасибо!"

Бонус
Использовать в print(sep='', end='')
Использовать в внутри print(переменную из input, sep='', end='')
"""

#for convenience, we move to a new line
print('Hi, User', end='!\n')
#We save user data
your_nick = input('Please enter your nickname:\n')
your_gender = input('Enter your gender:\n')
#translate into str for comparison operations
your_age = str(input('End your age:\n'))
#Movie tips not to write every time
star_wars_puck = 'I advise you to watch "Star Wars" or "Mandalorian"'
transform_puck = 'I advise you to watch "Transformers"'
insurgent_puck = 'I advise you to watch "Insurgent"'
tmnt_puck = 'I advise you to watch "TMNT"'

#Option for admin
if your_nick == "admin":
    print('Hi, my Lord!')
    if str(10) < your_age < str(14) and your_gender == 'man':
        print(star_wars_puck, end='!\n')
    elif your_age > str(30) and your_gender == 'man':
        print(star_wars_puck, end='!\n')
    elif str(22) < your_age < str(32) and your_gender == 'girls':
        print(transform_puck, end='!\n')
    elif your_age < str(16) and your_gender == 'girls':
        print(insurgent_puck, end='!\n')
    elif your_age < str(11) and your_gender == 'man':
        print(tmnt_puck, end='!\n')
#Option for Zhenya
elif your_nick == 'Zhenya':
    print('I advise you to watch "TENET"')

#Option for Guido
elif your_nick == 'Guido':
    print('Thank you very much', end='!')
    if str(10) < your_age < str(14) and your_gender == 'man':
        print(star_wars_puck, end='!\n',)
    elif your_age > str(30) and your_gender == 'man':
        print(star_wars_puck, end='!\n')
    elif str(22) < your_age < str(32) and your_gender == 'girls': #But what if he's a girl))
        print(transform_puck, end='!\n')
    elif your_age < str(16) and your_gender == 'girls':#But what if he's a girl))
        print(insurgent_puck, end='!\n')
    elif your_age < str(11) and your_gender == 'man':
        print(tmnt_puck, end='!\n')

#all Users
elif str(10) < your_age < str(14) and your_gender == 'man':
    print(star_wars_puck, end='!\n')
elif your_age > str(30) and your_gender == 'man':
    print(star_wars_puck, end='!\n')
elif str(22) < your_age < str(32) and your_gender == 'girls':
    print(transform_puck, end='!\n')
elif your_age < str(16) and your_gender == 'girls':
    print(insurgent_puck, end='!\n')
elif your_age < str(11) and your_gender == 'man':
    print(tmnt_puck, end='!\n')

"""
No options
And bonus 
"""
else:
    print('You', 'are', 'cunning', 'Mr or Misis', your_nick, sep='\n', end='!\n')
