'''Требуется найти в массиве из случайных чисел(от 1 до n) самый близкий
 по величине элемент к заданному числу X. Пользователь в первой строке вводит
 натуральное число N – количество элементов в массиве. 
Последняя строка содержит число X'''

N = int(input())
lst = map(int, (input().split()))
x = int(input())
print(min(lst, key=lambda a:abs(a-x)))

#a=[int(i) for i in input().split()]
#b=int(input())
#number=0
#for i in range(len(a)):
#   if (b-a[i])<b-number and b-a[i]>0:
#       number=i
#print(a[number])
