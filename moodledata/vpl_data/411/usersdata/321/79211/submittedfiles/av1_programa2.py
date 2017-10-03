# -*- coding: utf-8 -*-
#Entrada
a= float(input('Preço normal da etiqueta: '))
b= int(input('Condição de pagamento: '))

if b == 1:
    t= a - ((a * 15)/100)
    print('%.2f' % t)
elif b == 2:
    