# -*- coding: utf-8 -*-
from __future__ import division
n=input('digite a quantidade de elementos:')
l=[]

for i in range (0,n,1):
    l.append(input('digite um elemento'))
    
print(l[0])
print(l[n])

soma=0
i=0
while i<n:
    soma=soma+l[i]
    i=i+1
print(soma/len[l])

print(len[l])
