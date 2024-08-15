#1
first = int(input ("Введите число: "))
second = int(input("Введите число: "))
third = int(input("Введите число: "))
if first == second and second == third:
    print(3)
elif first == third:
    print(3)
else:
    print(False)
#2
first = int(input("Введите число: "))
second = int(input("Введите число: "))
third = int(input("Введите число: "))
if third == first or second == first:
    print(2)
elif first == second:
    print(2)
else:
    print(0)
# 3
first = int(input("Введите число: "))
second = int(input("Введите число: "))
third = int(input("Введите число: "))
if second == third or first == second:
    print(True)
elif first == third:
    print(True)
else:
    print(0)