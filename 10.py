# num_set={1,2,3,4,5}
# print(num_set)

# str_num={'Nic', "Tol", 'Luka', 'Moto'}
# print(str_num)

# mixed_set={1, 2, 3, 'Nik', 'Mike',(1,2,3)}
# print(mixed_set)

# num_set = set([1, 2, 3, 4, 5, 6])
# print(num_set)
# num_set=set([1,2,3,1,2]) #дубликаты не поддерживаются
# print(num_set)
# x=set()
# y={}
# print(type(x), type(y))

# x={1,2,3,4,5,6}
# for i in x:
#     print(i)

# x={'a','b','c','d','f'}
# x.add('E')
# print(x, 'a' in x)

# x={1,2,3,4,5,6}
# x.discard(8)
# print(x)
#
# x={1,2,3,4,5,6}
# x.remove(9)
# print(x)

# x={1,2,3,4,5,6}
# x.pop()
# print(x)
#
# x={1,2,3,4,5,6}
# x.clear()
# print(x)

# x={"a",'s','d','f'}
# y={'a','q','w','s',1,2}
# all_x=y.union(x)
# print(all_x)
# x={1,2,3,4,5,6}
# y={1,2,3,4,5,8}
# z={1,2,3,4,5,9}
# output=x.union(z,y)
# print(output)

# x={1,2,3,4,5,6}
# y={1,2,3,4,5,8}
# z={1,2,3,4,5,9}
# output=x|z|y
# print(output)

# x={1,2,3,4,5,6}
# y={1,2,3,4,5,8}
# z={1,2,3,4,5,9}
# print(x&z)

# x={1,2,3,4,5,6}
# y={1,2,3,4,5,8}
# print(x-y)
# print(y-x)

# str_set={'Nic', "Tol", 'Luka', 'Moto'}
# x=str_set.copy()
# print(x)

# x={'a','b','c','d','f'}
# str_set={'Nic', "Tol", 'Luka', 'Moto'}
# y=x.isdisjoint(str_set)
# print(y)

# x={'a','b','c','d','f'}
# print(len(x))

# x={'a','b','c','d','f'}
# y=frozenset(x)
# print(type(y))

#
# x=['a','b','c','d','f']
# y=['Nic', "Tol", 'Luka', 'Moto','a']
# a=set(x)
# b=set(y)
# dubl=a.isdisjoint(b)
# if dubl==True:
#     print('Dublikat - net')
# else:
#     print('Dublikat - yest')


x = {'a', 'b', 'c', 'd', 1, 2, 3}
a = {1, 2, 3, 4, 5}
y = frozenset(a)
z = x | y
d = x & y
print(z)
print(d)
