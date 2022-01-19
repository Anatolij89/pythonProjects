# while True:
#     a = float(input('Введите число: '))
#     d = input("Введите действие ")
#     b = float(input("Введите число "))
#     if d == "+":
#         elif d == "-":
#         print("a-b=", a - b)
#     elif d == ":" and b != 0:
#         print("a:b=", a / b)
#     elif d == ":" and b == 0:
#         print('"Ошибка деления на ноль"')
#     elif d == "*":
#         print("a*b=", a * b)
#     elif a == 0 or d == 0:
#         print('Выход')
#         break
#         print("a+b=", a + b)
import random
x = random.randint(0, 10)
c = random.randint(1, 2)
i=0
while True:
    d=int(input('Введите число: '))
    color=input('Введите цвет: ')
    if color=='red':
        color=1
    elif color=='black':
        color=2
    if d==x and c==color:
        print('Вы выиграли',x,c)
    i=i+1
    if i==5:
       print(x, c)
       break

