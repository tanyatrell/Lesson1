'''Задание 1

Измените функцию get_summ() чтобы результат 
выводился заглавными буквами использйте метод 'строка'.upper()'''

def get_summ(one, two, delimeter=' '): 
	return str(one).upper() + str(delimeter) + str(two).upper()

result = get_summ('Hello', 'world')
print(result)