# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite n: ')

l=[]
somaPar=0
contadorPar=0
somaImpar=0
contadorImpar=0

for i in range(0,n,1):
    l.append(input('Digite um elemento: '))
    
    if (l[i]%2==0):
        contadorPar=contadorPar+1
        somaPar=somaPar+l[i]
    
    else:
        contadorImpar=contadorImpar+1
        somaImpar=somaImpar+l[i]
    
print(somaImpar)
print(somaPar)
print(contadorImpar)
print(contadorPar)
print(l)



    
    