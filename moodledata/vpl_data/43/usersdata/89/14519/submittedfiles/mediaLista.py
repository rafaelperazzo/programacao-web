# -*- coding: utf-8 -*-
from __future__ import division

n=input('Digite n: ')

l=[]

for i in range(0,n,1):
    l.append(input('Digite um elemento: '))
    
print('%.2f' %l[0])
print('%.2f'%(l[len(1)-1]))

soma=0
for i in range(0,n,1):
    soma=soma+l[i]

media=soma/(len(l))
print('%.2f' %media)

print(l)











