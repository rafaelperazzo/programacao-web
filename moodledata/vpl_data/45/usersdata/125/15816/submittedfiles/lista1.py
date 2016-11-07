# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite um valor:')
a=[]

par=0
impar=0
somapar=0
somaimpar=0
cont_1=0
for i in range (0,n,1):
    a.append(input('digite um elemento:'))
if a[i]%2==1:
    par=par+1
    somarpar=somapar+1
else:
    impar=impar+1
    somarImpar=somaImpar+1
    
print ('numero de impares:%d', impar)
print ('numero de pares: %d', par)
print ('soma dos pares:%d/n',somapar)
print ('soma do impares: %d/n',somaImpares)
print ('a')
    