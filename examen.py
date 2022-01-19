# d=int(input("Введите 7-значное число: "))
# y=0 # четные
# s=0 #нечетные
# z=1 #произведение
# l=str(d)
# q=0
# for i in l:
#     i=int(i)
#     if i%2==0:
#         y=y+1
#     else:
#         s=s+1
# if y>s:
#     for k in l:
#         k=int(k)
#         q+=k    #сумма
#     print(q)
# else:
#     z=(int(l[0]))*(int(l[2]))*(int(l[5]))
#     print(z)
#
# # 2 задача
# l=input('Введите текст: ')
# a=0 # сумма гласных
# b=0 # сумма согласных
# lis=[]
# for i in l:
#     if i in 'aeoiu':
#         a+=1
#     else:
#         b+=1
# if a==b:
#     for k in l:
#         if k in 'aeoiu':
#             lis.append(k)
#     print(lis)
# print(a,b)

# Задача 3
import random

# import random
# rec=0
# m=0
# z=0
# i=0
# while i<6:
#     x1 = int(input('Введите 1-ое число 1...20: '))
#     x2 = int(input('Введите 2-ое число 1...20: '))
#     y1 = random.randint(1, 20)
#     y2 = random.randint(1, 20)
#     print(y1,y2)
#     i+=1
#     if i==4:
#         rec=(y1,y2)
#     if x1>y1 and x2>y2:
#         z+=1
#     else:
#         m+=1

# if z==m:
#     print('4 пара ',rec)
# else:
#     print('Количество' ,z)


# # # задача4
# import random
# z=0
# n=int(input("Введите количество: "))
# q= int(input('Введите цифру: '))
# a=[random.randint(0,100) for i in range(n)]
# print(a)
# for i in a:
#     for k in str(i):
#         if q==int(k):
#             z+=1
# print(z)
#
# # Задача 5
# a=input('Введите строку: ')
# print(a)
# b=''
# arr=[]
#
# for i in a:
#     if i.isdigit():
#         b+=i
#     elif b!='':
#         arr.append(b)
#         b=''
# if b!='':
#     arr.append(b)
# print(','.join(arr))
#
# Задача 6
a=input('Введите строку: ')
b=0
c=0
nr=0
vr=0
gl=0
sg=0
for i in a:
    if i.isupper():
        b+=1
        c=0
        if b==2:
            vr+=1
            b=0
    elif i.islower():
        c+=1
        b=0
        if c==2:
            nr+=1
            c=0
    elif i in 'aeoiu':
        gl+=1
sg=len(a)-gl
print(len(a), gl,nr,vr)






