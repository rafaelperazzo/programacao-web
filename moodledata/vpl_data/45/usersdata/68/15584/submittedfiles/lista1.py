# -*- coding: utf-8 -*-
from __future__ import division

n= input ('Digite o tamanho da lista:')
l=[]
i=0
somap=0
somai=0
contp=0
conti=0

while i<n:
    l.append (input('Digite um elemento da lista:'))
    i=i+1
for i in range (0, len (l),1):
    if l[i]%2==0:
        somap=somap+l[i]
    else:
        somai=somai+l[i]
    
for i in range (0, len (l),1):
    if l[i]%2==0:
        contp=contp+1
    else:
        conti=conti+1

print somai
print somap
print conti
print contp
print l