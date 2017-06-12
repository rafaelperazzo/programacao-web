# -*- coding: utf-8 -*-
from __future__ import division
n=int(input('digite o valor de n:'))
lista=[]
somai=0
somap=0
conti=0
contp=0
for i in range(1,n+1,1):
    valor=int(input('digite o valor:'))
    lista.append(valor)
for i in range(0,len(lista),1):
    if lista[i]%2!=0:
        somai=somai+lista[i]
        conti=conti+1
    else:
        somap=somap+lista[i]
        contp=contp+1
print(somai)
print(somap)
print(conti)
print(contp)
        
