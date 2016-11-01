# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite um número de base binária:'))

a=n
contador=0
for i in range (0,n,1):
    a=a//10
    contador=contador+1
print contador
    