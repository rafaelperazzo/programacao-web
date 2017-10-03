# -*- coding: utf-8 -*-
#COMECE AQUI ABAIXO
p= int(input('Digite o peso: '))
e= p - 50

if e <= 0:
    print('\nExcesso= ZERO')
    print('\nMulta= ZERO')
else :
    if e > 0:
    m= e * 4
    print('\nExcesso= %.f' % e)
    print('\nMulta= R$%.2f' % m))