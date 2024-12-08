# 1. Функция с параметрами по умолчанию
def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# Вызовы функции с разным количеством аргументов
print_params()  # Вызов без аргументов
print_params(10)  # Вызов с одним аргументом
print_params(10, 'новая строка')  # Вызов с двумя аргументами
print_params(b=25)  # Вызов с именованным аргументом
print_params(c=[1, 2, 3])  # Вызов с именованным аргументом

# 2. Распаковка параметров
values_list = [3.14, 'текст', False]
values_dict = {'a': 42, 'b': 'слово', 'c': None}

# Передача списка и словаря в функцию с распаковкой
print_params(*values_list)  # Распаковка списка
print_params(**values_dict)  # Распаковка словаря

# 3. Распаковка + отдельные параметры
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)  # Распаковка списка и передача дополнительного параметра
