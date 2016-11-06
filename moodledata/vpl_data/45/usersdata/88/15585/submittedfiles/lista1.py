# -*- coding: utf-8 -*-
from __future__ import division

n= int(input('digite o valor de n: '))
L=[]

for i in range(0,n,1):
    L.append(input('digite um numero: '))

cont=0
cont2=0
soma=0
soma2=0
for j in range(0,n,1):
    if L[j]%2==1:
        soma=soma+L[j]
        cont=cont+1
    else:
        soma2=soma2+L[j]
        cont2=cont2+1
print soma
print soma2
print cont
print cont2
print L

        


