Sklad={'aple':[1, 20],
       'orange':[1.2,15],
       'banan':[2.50,25],
       'lemon':[3,22]}
for i in Sklad:
     print(i,'-', Sklad[i][0],'p.', '-', Sklad[i][1],'kg')
while True:
    prod = input('Введите продукт: ')
    if prod == 'n':
        break
    elif prod in Sklad:
        masa=float(input('Введите кол-во товара: '))
        cena=Sklad[prod][0]
        cost=cena*masa
        masa_old=Sklad[prod][1]
        print(masa_old)
        masa_new=masa_old-masa
        Sklad[prod][1]=masa_new
        masa_old=masa_new
        print('Выбран: ',prod,'- ', cost,'p.', '-', masa, 'kg')
        for m in Sklad:
            print('Остаток: ',m, '-', Sklad[m][0], 'p.', '-', Sklad[m][1],'kg')





