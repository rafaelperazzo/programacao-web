# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite o saldo:'))
valor=0
if  0<a<=500:
    print('nenhum saldo')
if a>=501 or a<=1000:
    valor= valor+(0.3*a)
    print(valor)
if a>=1001 or a<=3000:
    valor=valor+(0.4*a)
    print(valor)
if a>3000:
    valor=valor+0.5*a
    print(valor)