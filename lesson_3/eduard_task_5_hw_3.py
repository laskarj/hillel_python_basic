"""
Задача 5 на 25 балов Программа получает пользовательский ввод: большой_текст
В тексте будут встречаться ругательства: "черт". При этом, ругательства могут быть написаны с использованием любого
регистра или с использованием двоих сразу.
Пример: Черт, чЕрт, черТ, ЧЕРТ и тд.
Вывести текст, заменив все отдельные слова "черт" на "####". Не беспокойтесь о регистре букв выводимого текста.
Так же текст будет без знаков припенания.
Учитывайте что в словах текста может встречаться последовательность "черт", которая является частью другого слова,
и такие последовательности за ругательства не считаются.
"""

user_txt = input('Pls Enter big text:').lower().replace('черт ', ' ####').replace(' черт', ' #### ')
print(user_txt)