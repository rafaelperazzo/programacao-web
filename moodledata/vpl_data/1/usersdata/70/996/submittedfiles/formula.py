# -*- coding: utf-8 -*-
from __future__ import division
#Entrada

P = input('Determine o valr de P: ')
i = input('Determine o valor de i: ')
n = input('Determine o valor de n: ')

#Processamento

v = P * (((((1+i)**n)-1))/i)

#Saida 

print('O valor de v é: %.2f' % v)