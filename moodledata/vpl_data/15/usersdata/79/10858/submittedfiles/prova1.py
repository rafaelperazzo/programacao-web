# -*- coding: utf-8 -*-
from __future__ import division
import math

#COMECE SEU CÓDIGO ABAIXO DESTA LINHA

#Entrada

a = input('Carta 1: ')
b = input('Carta 2: ')
c = input('Carta 3: ')
d = input('Carta 4: ')
e = input('Carta 5: ')

#Processamento e saída

if a > b > c > d > e:
    print('C')
    
elif a < b < c < d < e:
    print('D')
    
else:
    print('N')



