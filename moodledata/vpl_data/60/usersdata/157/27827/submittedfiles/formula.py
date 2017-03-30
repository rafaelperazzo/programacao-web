# -*- coding: utf-8 -*-
p=float(input('Digite o valor de P:'))
i=float(input('Digite o valor de I:'))
n=int(input('Digite o valor de N:'))
v=(p*((1+i)**n)-1)/i
print('%.2f'%v)