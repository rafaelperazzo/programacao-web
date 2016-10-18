# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite o valor de m: ')

soma = 3
i = 2
j = 3
k = 4
cont = 1

while cont<=m:
    if cont%2 != 0:
        soma = soma + (4/(i*j*k))
    else:
        soma = soma - (4/(i*j*k))
    
    i = i + 2
    j = j + 2
    k = k + 2
    cont = cont + 1
    
print ("%.6f" % soma)