# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de valores:')
l=[]


for i in range (0,n,1):
    l.append(input('Digite um elemento:'))

soma=0    
for i in range (0,n,1):
    soma=soma+l[i]
    
media=soma/n

print l[0]
print l[n]
print media

