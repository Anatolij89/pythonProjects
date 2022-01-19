# # 1
# a=[1,1,2,3,4,5,5,5]
# b=[]
# for i in a:
#      c=a.count(i)
#      if c==1:
#          b.append(i)
# print(b)

# 2
# a=[1,1,1,2,3,4,5,5]
# c=0
# for i in a:
#     x=a.count(i)
#     if x//2==0:
#         c=c+(x//2)
# print(c)

# 3
# c_1=(35, 78, 21, 37, 2, 98, 6, 100, 231)
# c_2=(45, 21, 124, 76, 5, 23, 91, 234)
# sum_a=sum(c_1)
# sum_b=sum(c_2)
# if sum_a>sum_b:
#     print('Сумма больше в кортеже-a')
# else:
#     print('Сумма больше в кортеже-b')
# print('Min:', c_1.index(min(c_1))+1,'Max:',c_1.index(max(c_1))+1 )
# print('Min:', c_2.index(min(c_2))+1, 'Max:',c_2.index(max(c_2))+1 )

## 4
# st='an apple a day keeps the doctor away'
# list_1=[]
# list_2=[]
# for i in st:
#     if i!=' ':
#         list_1.append(i)
# print(list_1)
# for k in list_1:
#     list_2.append(list_1.count(k))
# print(list_2)
# dict_1=dict(zip(list_1,list_2))
# print(dict_1)

# #5
# konditer={'пироженное':[1, 200],
#        'мафин':[1.2,150],
#        'торт':[2.50,250]}
# for i in konditer:
#      print(i,'-', konditer[i][0],'p.', '-', konditer[i][1],'g')
# while True:
#     zapros = input('Введите запрос: ')
#     if zapros == 'n':
#         break
#     elif zapros=='описание':
#         print(konditer.keys)
#     elif zapros==''

# #8
# suma=0
# n=0
# sr_bal=0
# with open('task_1.txt') as f:
#     d = f.readlines()
#     for i in d:
#         n+=1
#         i.replace('\n', '')
#         for k in i:
#             if k.isdigit():
#                 c=int(k)
#                 suma+=c
#                 if c<3:
#                     print('Ниже 3', i)
# sr_bal=suma/n
# print(sr_bal)



