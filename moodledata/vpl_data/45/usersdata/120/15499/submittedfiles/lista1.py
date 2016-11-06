# -*- coding: utf-8 -*-
from __future__ import division
#entrada
n=input('insira a quantidade de elementos:')
l=[]
#processamento
somai=o
somap=0
conti=0
contp=0
for i in range(0,n,1):
    l.append(input('digite um elemento:'))

for i in range(0,n,1):
    if i%2!=0:
        somai=somai+l[i]
        conti=conti+1
    if i%2==0:
        somap=somap+l[i]
        contp=contp+1
#saida
print somai
print somap
print conti
print contp
print(l)
