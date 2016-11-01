# -*- coding: utf-8 -*-
from __future__ import division

n=int(input('Digite o valor da quantidade de valores de n:'))

l=[]

for i in range(0,n,1):
    l.append(input('Digite o valores dos termos de n:'))
    media=i//n
i=i+1

print(l[0])
print(l[n-1])
print(media)
print(l) 
