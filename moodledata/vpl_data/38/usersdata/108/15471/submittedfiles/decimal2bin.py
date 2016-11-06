# -*- coding: utf-8 -*-
from __future__ import division

n = input ('Digite o valor de n:')
resto = n
contador = -1
a = 0

while (n>=0.9):
    n = n/10
    contador = contador+1

while (n>=0.01):
    n = n*10
    j = n//1
    a = a+((j*2)**contador)
    contador = contador-1
    n = n-j
    
print (a)
    

