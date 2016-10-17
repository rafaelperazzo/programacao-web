# -*- coding: utf-8 -*-
from __future__ import division
import math

m = input('Digite o numero de termos: ')
soma = 0
i = 1
den = 2

while i<=m :
    if i%2==0:
        soma = soma - 4/((den)*(den+1)*(den+2))
    else: 
        soma = soma + 4/((den)*(den+1)*(den+2))

    den = den+1
    i = i+1
pi = 3+soma
print ('%.6f'%pi)
print math pi