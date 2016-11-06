# -*- coding: utf-8 -*-
from __future__ import division
n=input('entre com o valor de n: ')
a=[]
somai=0
somap=0
conti=0
contp=0

for i in range (0,n,1):
    a.append(input('entre com o próxima valor da lista: '))
    if a[i]%2!=0:
        somai=somai+a[i]
        conti=conti+1
    elif a[i]%2==0:
        somap=somap+a[i]
        contp=contp+1
        
print somai
print somap
print conti
print contp
print a

