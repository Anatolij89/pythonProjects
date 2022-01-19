# import random
# x = random.randint(0, 5)
# a = int(input("Введите число "))
# if x == a:
#     print('Вы угадали')
# else:
#     print("Не угадали", x)
a=float(input("Введите число "))
d=input("Введите действие ")
b=float(input("Введите число "))
if d=="+":
    print("a+b=",a+b)
elif d=="-":
    print("a-b=",a-b)
elif d==":":
    print("a:b=",a/b)
elif d=="*":
    print("a*b=", a*b)
