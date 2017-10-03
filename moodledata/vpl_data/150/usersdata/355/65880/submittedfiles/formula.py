# -*- coding: utf-8 -*-
#ENTRADA
P = float(input('Digite P: '))
i = float(input('Digite i: '))
n = float(input('Digite n: '))
#PROCESSAMENTO
v = P*((((1+i)**n)-1)/i)
print('%.2f'%v)

