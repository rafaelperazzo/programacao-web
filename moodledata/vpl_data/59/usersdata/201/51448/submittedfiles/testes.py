# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
n=float(input('Depósito inicial:'))
t=float(input('Taxa de juros:'))
for i in range(1,25,1):
    n=n+(n*t)
    print('R$%.2f'%n)