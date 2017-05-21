# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite o saldo:'))
valor=0
if  0<a<=500:
    print('nenhum saldo')
if 501<=a<=1000:
    valor= valor+(0.3*a)
    print(valor)
if 1001<=a<=3000:
    valor=valor+(0.4*a)
    print(valor)
if a>3000:
    valor=valor+0.5*a
    print(valor)