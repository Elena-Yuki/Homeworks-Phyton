def print_params(a=1, b="строка", c=True):
    print(a, b, c)

print_params(2, 6,8,)


values_list = [777, "hard", (2,3,8)]
values_dict = {"a": 34, "b": "page", "c": "88"}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, "Строка"]
print_params(*values_list_2, 42)





