# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
s= float(input('Salário bruto: '))
p= float(input('Prestação: '))

po= (p * 100)/s

if po <= 30 :
    print('Concedido')
else :
    print('Não concedido')