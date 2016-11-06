# -*- coding: utf-8 -*-
from __future__ import division
#entrada
n=input('insira a quantidade de elementos:')
l=[]
#processamento
for i in range(0,n,1):
    l.append(input('digite um elemento:'))
somai=0
somap=0
cont=0
i=0
for i in range(0,n,1):
    if i%2!=0:
        somai=somai+l[i]
        conti=cont+1
    if i%2==0:
        somap=somap+l[i]
        contp=cont+1
#saida
print somai
print somap
print conti
print contp
print(l)
