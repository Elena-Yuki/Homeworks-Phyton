# Словари
my_dict = {"Food": "eggplant", "Friends": "Dariya", "numbers":89645321098, "cities": "Волгоград"}
print(my_dict)
print(my_dict.get("cities"))
print(my_dict.get("Language", 1000))
my_dict.update({"Students": "Jimmy", "Years": 2002 })
print(my_dict)
f = my_dict.pop("Food")
print(f)
print(my_dict)
# Множества
my_set = {8, 7, 0, 76, 8, 7, 76, "wanted", (4, 5, 6)}
print(my_set)
print(my_set.add(87))
print(my_set.add("apple"))
print(my_set)
print(my_set.remove(8))
print(my_set)
