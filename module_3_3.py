# Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Разные вызовы функции с параметрами по умолчанию
print_params()
print_params(b=25)
print_params(c=[1, 2, 3])

# Распаковка параметров
values_list = [100, 'пример строки', False]
values_dict = {'a': 45.67, 'b': 'другой текст', 'c': None}

print_params(*values_list)
print_params(**values_dict)

# Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42) 