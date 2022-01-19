elements=[15,48,'hello',6,19,'world']
a=['a','e','y','u','i','o'] #список гласные
x=0 # четные числа
y=0 # нечетные числа
d=[]
for i in elements:
    if type(i) is int:
        if i%2==0:
            i=str(i)
            for k in i:
                k=int(k)
                y += k
            print('сумма четных ', y)
