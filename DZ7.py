# # Задача 1
# a = 'a asdfd ewuir hksdla'
# b = a.split(' ')
# print(b, 'Самое длиное слово: ', max(b, key=len))

# Задача 2
a = 'abc, qwert; fgh:'
b = a.split(' ')
x=0
c=[]
d=[]
print(b)
for i in b:
    print(i)
    for k in i:
        if (k.isdigit()==False and k.isalpha()==False) or k==" ":
            print(k)
            x+=1
        else:
                c.append(k)
        if x!=0:
                d.append(''.join(c))
                c=[]
                x=0
print(d)




