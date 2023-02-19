'''Требуется определить, можно ли от шоколадки размером n × m долек отломить 
k долек, если разрешается сделать один разлом по прямой между дольками 
(то есть разломить шоколадку на два прямоугольника).
*Пример:*
3 2 4 -> yes
3 2 1 -> no'''

'''n = int(input())
m = int(input())
k = int(input())
oppor_vert = "NO"
oppor_hor = "NO"
for x in range (n-1):
    left = (x+1)*m
    right = n*m - left
    if k == left or k == right:
        oppor_vert = ("YES")
for y in range (m-1):
    up = (y+1)*n
    down = n*m - up
    if k == up or k == down:
        oppor_hor = "YES"
if oppor_hor == "YES" or oppor_vert == "YES":
    print ("YES")
else:
    print("NO")'''

n = int(input('Введите ширину шоколадки: '))
m = int(input('Введите длину шоколадки: '))
k = int(input('Введите количество кусочков шоколадки: '))   
if k <= m*n and (k%m==0 or k%n==0):
    print('Можно получить это количество кусочков: ')
else:
    print('Нельзя получить это количество кусочков: ')