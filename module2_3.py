# "Ноль ничто отрицание не допустимо"
my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
y = 0
while  my_list[y] >= 0 and y < len(my_list):
    if my_list[y] > 0:
        print(my_list[y])
    y+=1
    if y == len (my_list):
        break


print(my_list) 













