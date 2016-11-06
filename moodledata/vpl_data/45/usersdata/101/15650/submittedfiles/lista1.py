# -*- coding: utf-8 -*-
from __future__ import division

n = input('Digite o valor de n: ')
a = []

somaI = 0
somaP = 0
contI = 0
contP = 0

for i in range (0,n,1):
    a.append(input('Digite o próximo elemento da lista: ')
    if a[i]%2!=0:
        somaI = somaI + a[i] 
        contI = contI + 1
    if a[i]%2==0:
        somaP = somaP + a[i] 
        contP = contP + 1
        

print (somaI)
print (somaP)
print (contI)
print (contP)
print(a)
        
    