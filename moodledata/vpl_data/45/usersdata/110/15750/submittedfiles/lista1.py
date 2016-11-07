# -*- coding: utf-8 -*-
from __future__ import division
n=input('Digite n: ')
a=[]
somai=0
somap=0
conti=0
contp=0
for i in range(0,n,1):
    a.append(input('Digite o valor: '))
for i in range(0,len(a),1):
    if a[i]%2==0:
        somap=somap+a[i]
        contp=contp+1
    else:
        somai=somai+a[1]
        conti=conti+1
print(somai)
print(somap)
print(conti)
print(contp)
print(a)
