# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de valores:')
a=[]

for i in range(0,n,1):
    a.append(input('Digite valores a lista:'))

impares=0
contadorImpares=0
pares=0
contadorPares=0

for i in range(0,n,1):
    if a[i]%2==0:
        pares=pares+a[i]
        contadorPares=contadorPares+1
        
    else:
        impares=impares+a[i]
        contadorImpares=contadorImpares+1
        
print(impares)
print(pares)
print(contadorImpares)
print(contadorPares)
print(a)