# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite o valor de n:'))

l=[]

somap=0
somai=0
contp=0
conti=0

for i in range (0,n,1):
    l.append(input('Digite o valor de cada elemento:'))
    
for i in range (0,n,1):
    
    if l[i]%2==0:
        contp=contp+1
        soma=soma+l[i]
        
    else:
        conti=conti+1
        somai=soma+l[i]
print (somai)
print (somap)
print (conti)
print (contp)
print (l)