'''Даны два неупорядоченных набора целых чисел (может быть, с повторениями). 
Выдать без повторений в порядке возрастания все те числа, которые встречаются в 
обоих наборах. Пользователь вводит 2 списка. 1 строка - первый список через пробел.
2 строка - второй список через пробел.'''

num_list_1 = [1, 2, 6]
num_list_2 = [37, 3, 2]
num_list3 = num_list_1+num_list_2
print(num_list3)
kool = num_list3 = list(set(num_list3))
kool.sort()
print(num_list3)




