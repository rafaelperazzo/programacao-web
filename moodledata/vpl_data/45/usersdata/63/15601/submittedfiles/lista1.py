# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de valores:')
a=[]

for i in range(0,n,1):
    a.append('Digite valores a lista')
    
pares=0
contadorPares=0
for i in range(0,n,1):
    if n%2==0:
        pares=pares+a[i]
        contadorPares=contadorPares+1
        
ímpares=0
contadorÍmpares=0
for i in range(0,n,1):
    if n%2==1:
        ímpares=ímpares+a[i]
        contadorÍmpares=contadorÍmpares+1
        
print(ímpares)
print(pares)
print(contadorÍmpares)
print(contadorPares)
print(a)