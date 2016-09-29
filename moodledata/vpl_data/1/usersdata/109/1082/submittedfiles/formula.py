# -*- coding: utf-8 -*-
from __future__ import division

#Entrada
P = input('Digite o valo de P:')
i = input('Digite o valo de i:')
n = input('Digite o valor de n:')

#Processamento
v = P*(((1+i)**n)-1)/(i)

#Saída
print('%.2f'%v)
