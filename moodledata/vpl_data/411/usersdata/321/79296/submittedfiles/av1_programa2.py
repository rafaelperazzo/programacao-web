# -*- coding: utf-8 -*-
#Entrada
a= float(input('Preço normal da etiqueta: '))

b= int(input('Condição de pagamento: '))


#Saídas
if b == 1:
    t= a - ((a * 15)/100)
    print('%.2f' % t)
elif b == 2:
    to= a - ((a * 10)/100)
    print('%.2f' % to)
elif b == 3:
    print('%.2f' % a)
elif b == 4:
    total= a + ((a * 10)/100)
    print('%.2f' % total)