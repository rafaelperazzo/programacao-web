# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite a quantidade de termos:')
a = []
Somapar = 0
Somaimpar = 0
contadorpar = 0
contadorimpar = 0
for i in range (0,n,1):
    a.append ( input('Digite um número:'))
    if i%2==0:
        contadorpar = contadorpar +1
        Somapar = Somapar + a[i]
    elif i%2 != 0:
        contadorimpar = contadorimpar + 1
        Somaimpar = Somaimpar + a[i]
print (Somaimpar)
print (Somapar)
print (contadorimpar)
print (contadorpar)
print (a)