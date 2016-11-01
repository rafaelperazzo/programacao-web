# -*- coding: utf-8 -*-
from __future__ import division

n=input('digite a quantidade de elementos:')
l=[]

for i in range (0,n,1):
    l.append(input('digite o elemento:'))
    
soma=0
for i in range (0,n,1):
    soma=(soma+l[i])
media=((soma)/(len(1)))

print('%.2f'%l[0])
print('%.2f'%l[len(l)-1])
print('%.2f'%media)
print(l)