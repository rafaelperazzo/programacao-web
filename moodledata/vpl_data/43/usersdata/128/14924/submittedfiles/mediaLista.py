# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite a quantidade de termos: ')

l=[]
soma=0

for i in range (0,n,1):
    l.append(input('Digite um termo: '))
    soma=soma+l[i]

media=soma/n
print l[0]
print l[n-1]
print media
print l