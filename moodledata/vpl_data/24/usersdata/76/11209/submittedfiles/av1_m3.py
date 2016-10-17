# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite o valor de m:')

a = 2
b = 3
c = 4
soma = 3
contador = 1

while contador<=m:

    if contador%2 == 0:
        soma = soma - (4/(a*b*c))
    else:
        soma = soma + (4/(a*b*c))
       
    a = a + 2
    b = b + 2
    c = c + 2
    contador = contador + 1
    
print('%.6f' % soma)