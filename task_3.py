# Дано натуральное число. Требуется определить, 
# является ли год с данным номером високосным. 
# Если год является високосным, то выведите YES, иначе выведите NO. 
# Напомним, что в соответствии с григорианским календарем, 
# год является високосным, если его номер кратен 4, но не кратен 100,
# а также если он кратен 400.

# Input: 2016
# Output: YES

year = int(input())

#four_and_hund = (year % 4 == 0 and year % 100 != 0)
#four_h = (year % 400 == 0)
#if four_and_hund or four_h:

if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
    print('Yes')
else:
    print('No')

#def correct_int() -> int
    #is_correct = True
    #while is_correct:
        #a = input() # в а попасть целое число, но в а введено не int
        #try:
            #a = int(a)
            #is_correct = False
            #return a   
        #except ValueError:
            #ptint('некорректный ввод')
#s = correct_int()
#print(s)

