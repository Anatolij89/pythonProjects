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


l=input('Введите текст: ')
a=0
b=0
for i in l:
    if i in 'aeoiu':
        a+=1
    else:
        b+=1
if a==b:
    for k in l:
print(a,b)