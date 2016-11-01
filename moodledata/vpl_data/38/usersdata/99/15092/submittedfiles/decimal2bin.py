# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite um número de base binária:'))

contador=0
for i in range (0,n,1):
    n=n%10
    contador=contador+1
print contador
    