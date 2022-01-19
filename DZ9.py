Sklad=dict()
while True:
     prod = input('Введите продукт: ')
     if prod=='n':
         break
     elif prod not in Sklad:
          cena = float(input('Введите цена за кг: '))
          masa = float(input('Введите вес: '))
          cost=cena*masa #общая стоимость
          Sklad[prod]=cost,masa
          print(Sklad[prod])
     elif prod in Sklad:
         masa_new = float(input('Введите вес: '))
         masa=masa+masa_new
         cost=cena*masa
         Sklad[prod]=cost, masa
         print(Sklad[prod])

print(Sklad)
for i in Sklad:
     print('Наименование:',i,'-', Sklad[i][0],'p.', '-', Sklad[i][1], 'kg')

