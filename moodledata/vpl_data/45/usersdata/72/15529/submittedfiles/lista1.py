# -*- coding: utf-8 -*-
from __future__ import division
#ENTRADA
n=input('digite o valor de n:')
a=[]
somai=0
somap=0
conti=0
contp=0

#PROCESSAMENTO
for i in range (0,n,1):
    a.append(input('digite o valor do proximo termo:'))
    if a[i]%2!=0:
        somai=somai+a[i]
        conti=conti+1
    if a[i]%2==0:
        somap=somap+a[i]
        contp=contp+1
        
#SAIDA
print somai
print somap
print conti
print contp
        
        
