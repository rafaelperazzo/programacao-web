# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
p= int(input('Digite o peso: '))
e= p - 50

if e <= 0:
    print('Excesso= ZERO')
    print('Multa= ZERO')
else :
    if e > 0:
        m = e * 4
    print('Excesso= %.f' % e)
    print('Multa= R$%.2f' % m)