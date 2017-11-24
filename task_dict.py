'''Задание

Создайте словарь weather с ключами city, temperature, wind 
и значениями Москва, 20, восточный
Выведите на экран значение по ключу city
Измените значение температуры и выведите на экран новое значение
Посчитайте количество элементов словаря
Проверьте, есть ли в словаре ключ country
Добавьте в словарь элемент date со значением '27.05.2017'
Создайте список, добавьте туда три словаря с погодой за разные даты 
при помощи append()'''

weather = {
'city': 'Moscow', 
'temper': '20', 
'wind': 'ost'
}
print(weather['city'])

weather['temper']='25'
print(weather['temper'])

print(len(weather))
weather.get('country', 'No')
weather['date'] = '27.05.2017'
All_weathers = []
All_weathers.append(weather)

weather2 = {'city': 'Moscow', 'temper': '20', 'wind': 'ost', 'date': '22.10.2017'}
weather3 = {'city': 'Moscow', 'temper': '20', 'wind': 'ost', 'date': '23.10.2017'}
All_weathers.append(weather2)
All_weathers.append(weather3)
print(All_weathers)
