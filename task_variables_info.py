'''Информация о пользователе

В файле info.py создайте переменную user_info.
Запишите в неё словарь с полями first_name и last_name.
Попросите пользователя ввести его имя, его запишите в поле first_name словаря user_info.
Попросите пользователя ввести его фамилию, его запишите в поле last_name словаря user_info.
Выведите весь словарь на экран.
Запустите скрипт.'''

user_info = {'first_name': '', 'last_name': ''}
user_info['first_name'] = input('Введите имя: ')
user_info['last_name'] = input('Введите фамилию: ')
print(user_info)