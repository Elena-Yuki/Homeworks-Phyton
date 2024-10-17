def apply_all_func(int_list, *functions): #создаем функцию
    results = {} # создаем пустой словарь
    for func in functions: # с помощью цикла for перебираем функции из *functions
        results[func.__name__] = func(int_list) # обращаемся к атрибуту __name__ для того чтобы вять название функции
    return results # возвращаем словарь

# Проверяем работу кода
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))




