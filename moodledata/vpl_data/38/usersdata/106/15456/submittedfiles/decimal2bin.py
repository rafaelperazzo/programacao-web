# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite um número na base binária:')
contador = 0
a = n
while n>=1:
    contador = contador +1
    n= n//10
print (contador)