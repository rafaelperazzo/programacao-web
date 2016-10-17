# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite o valor de m: ')

soma = 0
i = 2
j = 3
k = 4

while i<=m:
    if i%2 == 0:
        soma = soma + 3
        soma = soma - (4/(i*j*k))
    else:
        soma = soma + (4/(i*j*k))
    
    i = i + 2
    j = j + 2
    k = k + 2
    
print ("%.6f" % soma)