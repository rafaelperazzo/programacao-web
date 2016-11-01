# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite um número de base binária:'))

a=n
contador=0
i=0
while i<a:
    a=a//10
    contador=contador+1
print (contador)
    