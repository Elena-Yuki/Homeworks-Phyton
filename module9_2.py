first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

first_result = [len(i) for i in first_strings if len(i) > 5]
# создаем список из длинн строк при условии что длина строк не менее 5 символов
print(first_result)
second_result = [(i, j) for i in first_strings for j in second_strings if len(i) == len(j)]
# при помощи двух циклов for перебираем два верхних списка и создаем сборки из кортежей слов одинаковой длинны
print(second_result)
third_result = {i: len(i) for i in first_strings + second_strings if len(i)%2 == 0}
# записываем словарь созданный при помощи сборки, где парой ключ-значение будет строка-длина строки
print(third_result)

