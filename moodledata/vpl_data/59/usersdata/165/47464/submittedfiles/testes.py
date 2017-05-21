# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
a=int(input('digite o saldo:'))
valor=0
if a>=0 or a<=500:
    print('nenhum saldo')
elif a>=501 or a<=1000:
    valor= valor+(0.3*a)
    print(valor)
elif a>=1001 or a<=3000:
    valor=valor+(0.4*a)
    print(valor)
else:
    valor=valor+0.5*a
    print(valor)